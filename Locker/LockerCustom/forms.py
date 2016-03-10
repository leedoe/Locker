from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import Form
from django.http import HttpResponse


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=8,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'ID',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )


class LockerDetailForm(Form):
    Locker = None
    LockerDetail = None

    def get_locker(self, locker, locker_detail):
        self.Locker = locker
        self.LockerDetail = locker_detail

    def parse_html(self):
        html = ""
        for i in range(1, self.Locker.rNum + 1):
            html += "<tr>"
            for j in range(1, self.Locker.cNum + 1):
                item = self.LockerDetail.get(row=i, column=j)
                html += "<td>" + str(item.locker_detail_number) + "<br/>"
                if item.check == 1:
                    html += "<button type='submit' value='" + str(item.id) + "' name='detail_id'>예약가능</button>"
                else:
                    html += "<button type='submit' value='" + str(item.id) + "' name='detail_id' disabled>예약불가</button>"
                html += "</td>"
            html += "</tr>"

        return html
