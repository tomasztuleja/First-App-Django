from django.test import TestCase
from .models import CustomUser
from django.db.utils import IntegrityError
from django.utils import timezone
from django.shortcuts import reverse
from django.test import Client
from .forms import CustomUserCreationForm


class CustomUserModelFieldsTests(TestCase):
    def setUp(self):
        """Function which will be called in every test functions"""
        self.created_user = CustomUser.objects.create(first_name="some_first_name",
                                                      last_name="some_last_name",
                                                      username="some_nickname",
                                                      email="some_email@gmail.com",
                                                      sex=1,
                                                      )

    # Testing fields of CustomUser model
    def test_if_created_user_has_valid_pk(self):
        self.assertEquals(self.created_user.pk, 1)

    def test_if_created_user_has_valid_first_name(self):
        self.assertEquals(self.created_user.first_name, "some_first_name")

    def test_if_created_user_has_valid_last_name(self):
        self.assertEquals(self.created_user.last_name, "some_last_name")

    def test_if_created_user_has_valid_username(self):
        self.assertEquals(self.created_user.username, "some_nickname")

    def test_if_created_user_has_valid_email(self):
        self.assertEquals(self.created_user.email, "some_email@gmail.com")

    def test_if_created_user_has_valid_sex(self):
        self.assertEquals(self.created_user.sex, 1)

    def test_if_date_joined_is_valid(self):
        self.assertLessEqual(self.created_user.date_joined, timezone.now())

    def test_if_created_users_staff_field_is_false(self):
        """Checking if created user cannot log in into admin page"""
        self.assertFalse(self.created_user.is_staff)


# Testing creation of CustomUser model
class RegistrationUserTests(TestCase):
    def setUp(self):
        """Function which will be called in every test functions"""
        self.created_user = CustomUser.objects.create(first_name="some_first_name",
                                                      last_name="some_last_name",
                                                      username="some_nickname",
                                                      email="some_email@gmail.com",
                                                      sex=1,
                                                      )

    def test_if_it_is_possible_to_create_user_with_already_used_username(self):
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create(first_name="some_first_name",
                                      last_name="some_last_name",
                                      username="some_nickname",
                                      email="some_second_email@gmail.com",
                                      sex=1,
                                      )

    def test_if_it_is_possible_to_create_user_with_already_used_email(self):
        with self.assertRaises(IntegrityError):
            CustomUser.objects.create(first_name="some_first_name",
                                      last_name="some_last_name",
                                      username="some_second_nickname",
                                      email="some_email@gmail.com",
                                      sex=1,
                                      )


class TemplatesAddressesStatusCodeTests(TestCase):
    def test_if_status_code_of_home_page_get_by_name_of_template_is_200(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_if_status_code_of_home_page_get_by_url_address_is_200(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEquals(response.status_code, 200)

    def test_if_status_code_of_registration_page_get_by_name_of_template_is_200(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    def test_if_status_code_of_registration_page_get_by_url_address_is_200(self):
        response = self.client.get('http://127.0.0.1:8000/register')
        self.assertEquals(response.status_code, 200)

    def test_if_status_code_of_login_page_get_by_name_of_template_is_200(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    def test_if_status_code_of_login_page_get_by_url_address_is_200(self):
        response = self.client.get('http://127.0.0.1:8000/login')
        self.assertEquals(response.status_code, 200)

    def test_if_status_code_of_logout_page_get_by_name_of_template_is_200(self):
        response = self.client.get(reverse('logout'))
        expected_url = reverse('home')
        self.assertRedirects(response,
                             expected_url,
                             status_code=302,
                             target_status_code=200,
                             msg_prefix='',
                             fetch_redirect_response=True,
                             )

    def test_if_status_code_of_logout_page_get_by_url_address_is_200(self):
        response = self.client.get('http://127.0.0.1:8000/logout')
        expected_url = reverse('home')
        self.assertRedirects(response,
                             expected_url,
                             status_code=302,
                             target_status_code=200,
                             msg_prefix='',
                             fetch_redirect_response=True,
                             )

    def test_if_status_code_of_edit_profile_page_for_anonymous_user_is_404(self):
        created_user = CustomUser.objects.create(first_name="some_first_name",
                                                 last_name="some_last_name",
                                                 username="some_nickname",
                                                 email="some_email@gmail.com",
                                                 sex=1,
                                                 )
        response = self.client.get('http://127.0.0.1:8000/edit_profile/' + created_user.username)
        self.assertEquals(response.status_code, 404)


class LoggedInUserTestsByLoginForm(TestCase):
    def setUp(self):
        self.created_user = CustomUser.objects.create(first_name="some_first_name",
                                                      last_name="some_last_name",
                                                      username="some_nickname",
                                                      email="some_email@gmail.com",
                                                      password="1234",
                                                      sex=1,
                                                      )
        self.created_user.set_password('1234')
        self.created_user.save()
        self.c = Client()
        self.response = self.c.post(reverse('login'), {'username': 'some_nickname', 'password': '1234'})

    def test_log_in(self):
        is_logged_in = self.c.login(username="some_nickname", password="1234")
        self.assertTrue(is_logged_in)

    def test_redirection_after_log_in(self):
        pass


class LoggedInUserTests(TestCase):
    def setUp(self):
        self.login = self.client.force_login(CustomUser.objects.get_or_create(first_name="some_first_name",
                                                                              last_name="some_last_name",
                                                                              username="some_nickname",
                                                                              email="some_email@gmail.com",
                                                                              password="1234",
                                                                              sex=1,
                                                                              )[0])

    def test_if_only_logged_in_user_can_get_his_profile_info_page(self):
        response = self.client.get(reverse('edit_profile', kwargs={'slug': 'some_nickname'}))
        self.assertEquals(response.status_code, 200)


class FormsTests(TestCase):
    # REGISTER FORM
    def test_register_form(self):
        form_data = {'username': 'some_nickname',
                     'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password1': 'some_password10',
                     'password2': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_register_form_when_first_name_was_not_input(self):
        form_data = {'username': 'some_nickname',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password1': 'some_password10',
                     'password2': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_when_last_name_was_not_input(self):
        form_data = {'username': 'some_nickname',
                     'first_name': 'some_first_name',
                     'email': 'some_email@gmail.com',
                     'password1': 'some_password10',
                     'password2': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_when_username_was_not_input(self):
        form_data = {'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password1': 'some_password10',
                     'password2': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_when_password_was_not_input(self):
        form_data = {'username': 'some_nickname',
                     'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password2': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_when_password2_was_not_input(self):
        form_data = {'username': 'some_nickname',
                     'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password1': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_with_password_expectations(self):
        form_data = {'username': 'some_nickname',
                     'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password1': 's',
                     'password2': 's',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_when_password_and_password2_are_not_equal(self):
        form_data = {'username': 'some_nickname',
                     'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password1': 'some_password10',
                     'password2': 'some_password',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_when_username_is_already_in_use(self):
        CustomUser.objects.create(first_name="some_first_name",
                                  last_name="some_last_name",
                                  username="some_nickname",
                                  email="some_email@gmail.com",
                                  sex=1,
                                  )
        form_data = {'username': 'some_nickname',
                     'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_other_email@gmail.com',
                     'password1': 'some_password10',
                     'password2': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_register_form_when_email_is_already_in_use(self):
        CustomUser.objects.create(first_name="some_first_name",
                                  last_name="some_last_name",
                                  username="some_nickname",
                                  email="some_email@gmail.com",
                                  sex=1,
                                  )
        form_data = {'username': 'some_other_nickname',
                     'first_name': 'some_first_name',
                     'last_name': 'some_last_name',
                     'email': 'some_email@gmail.com',
                     'password1': 'some_password10',
                     'password2': 'some_password10',
                     'sex': 1,
                     }
        form = CustomUserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
