# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import url_for

from albumy.models import User
from albumy.settings import Operations
from albumy.utils import generate_token
from tests.base import BaseTestCase


class AuthTestCase(BaseTestCase):

    def test_login_normal_user(self):
        response = self.login()
        data = response.get_data(as_text=True)
        self.assertIn('Login success.', data)

    # def test_login_locked_user(self):
    #     self.login(email='locked@helloflask.com', password='123')
    #     response = self.client.get(url_for('user.index', username='locked'))
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Your account is locked.', data)
    #
    # def test_login_blocked_user(self):
    #     response = self.login(email='blocked@helloflask.com', password='123')
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Your account is blocked.', data)
    #
    # def test_fail_login(self):
    #     response = self.login(email='wrong-username@helloflask.com', password='wrong-password')
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Invalid email or password.', data)
    #
    # def test_logout_user(self):
    #     self.login()
    #     response = self.logout()
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Logout success.', data)
    #
    # def test_login_protect(self):
    #     response = self.client.get(url_for('main.upload'), follow_redirects=True)
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Please log in to access this page.', data)
    #
    # def test_unconfirmed_user_permission(self):
    #     self.login(email='unconfirmed@helloflask.com', password='123')
    #     response = self.client.get(url_for('main.upload'), follow_redirects=True)
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Please confirm your account first.', data)
    #
    # def test_locked_user_permission(self):
    #     self.login(email='locked@helloflask.com', password='123')
    #     response = self.client.get(url_for('main.upload'), follow_redirects=True)
    #     self.assertEqual(response.status_code, 403)
    #
    # def test_register_account(self):
    #     response = self.client.post(url_for('auth.register'), data=dict(
    #         name='Grey Li',
    #         email='test@helloflask.com',
    #         username='test',
    #         password='12345678',
    #         password2='12345678'
    #     ), follow_redirects=True)
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Confirm email sent, check your inbox.', data)
    #

    # def test_bad_confirm_token(self):
    #     self.login(email='unconfirmed@helloflask.com', password='123')
    #     response = self.client.get(url_for('auth.confirm', token='bad token'), follow_redirects=True)
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Invalid or expired token.', data)
    #     self.assertNotIn('Account confirmed.', data)
    #
    #
    #
    #     # bad token
    #     response = self.client.post(url_for('auth.reset_password', token='bad token'), data=dict(
    #         email='normal@helloflask.com',
    #         password='new-password',
    #         password2='new-password'
    #     ), follow_redirects=True)
    #     data = response.get_data(as_text=True)
    #     self.assertIn('Invalid or expired link.', data)
    #     self.assertNotIn('Password updated.', data)
