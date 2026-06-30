from xml.dom import ValidationErr


class PasswordValidator:

    def validate(self, password, user=None):
        if 'password' in password:
            raise ValidationErr('The password should not contain the word "password"')


    def get_help_text(self):
        return 'The password should not contain the word "password"'



