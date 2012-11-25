from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from sentry.conf import settings
from sentry.plugins.bases.notify import NotificationPlugin

from sentry_comments import VERSION
from sentry_comments.forms import CommentConfForm
from sentry_comments.models import GroupComments


class CommentsPlugin(NotificationPlugin):
    """Comments plugin."""

    title = _('Comments')
    slug = 'comments'
    description = _('Add comments to sentry events.')
    version = VERSION

    conf_title = title
    conf_key = slug
    project_conf_form = CommentConfForm

    author = 'Andi Albrecht'
    author_url = 'https://github.com/andialbrecht/sentry-comments'

    resource_links = [
        (_('Documentation'), 'http://sentry-comments.readthedocs.org'),
        (_('Bug Tracker'), 'https://github.com/andialbrecht/sentry-comments/issues'),
        (_('Source'), 'https://github.com/andialbrecht/sentry-comments'),
    ]

    def get_title(self, group=None):
        """Adds number of comments to title."""
        title = super(CommentsPlugin, self).get_title()
        if group is not None:
            count = GroupComments.objects.filter(group=group).count()
        else:
            count = None
        if count:
            title = u'%s (%d)' % (title, count)
        return title

    def panels(self, request, group, panel_list, **kwargs):
        """Panel configuration:"""
        panel_list.append((self.get_title(group), self.get_url(group)))
        return panel_list

    def view(self, request, group, **kwargs):
        """Display and store comments."""
        if request.method == 'POST':
            message = request.POST.get('message')
            if message is not None and message.strip():
                comment = GroupComments(group=group, author=request.user,
                                        message=message.strip())
                comment.save()
                self._send_mail(comment, group)
        return self.render('sentry_comments/index.html', {
            'comments': GroupComments.objects.filter(group=group).order_by('-created'),
            'group': group,
        })

    def notify_users(self, group, event, **kwargs):
        """Does nothing.

        The plugin interface requires this method to be
        implemented. Since we don't send notifications when an event
        occurs, this implementation simply does nothing.
        """
        pass

    def should_notify(self, group, event):
        """Returns False.

        This plugin never notifies on events, but on comments.
        """
        return False

    def get_form_initial(self, project=None):
        return {'send_to_members': False}

    def _send_mail(self, comment, group):
        recipients = self.get_send_to(group.project)
        if not recipients:
            return
        author = comment.author.get_full_name() or comment.author.username
        subject_prefix = self.get_option('subject_prefix', group.project) or settings.EMAIL_SUBJECT_PREFIX
        subject = _('%(author)s added a comment') % {'author': author}
        link = '%s/%s/group/%d/actions/comments/' % (settings.URL_PREFIX, group.project.slug, group.id)
        body = render_to_string('sentry_comments/emails/comment.txt', {
            'group': group, 'comment': comment, 'link': link,
            'author': author})

        msg = EmailMultiAlternatives(
            '%s%s' % (subject_prefix, subject),
            body,
            settings.SERVER_EMAIL,
            recipients)
        msg.send()
