import os
from typing import List
from requests import Response, post

FAILED_LOAD_API_KEY = "Failed to Load MailGun API Key"
FAILED_LOAD_DOMAIN = "Failed to Load MailGun Domain"
ERROR_SENDING_EMAIL = "Error in sending cinfirmation email"

class MailGunException(Exception):
	def __init__(self, message: str):
		super().__init__(message)


class Mailgun:

	MAILGUN_DOMAIN = os.environ.get("MAILGUN_DOMAIN")
	MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
	FROM_TITLE = os.environ.get("FROM_TITLE")
	FROM_EMAIL = os.environ.get("FROM_EMAIL")

	@classmethod
	def send_email(cls, email: List[str], subject: str, text:str, html:str) -> Response:

		if cls.MAILGUN_API_KEY is None:
			raise MailGunException(FAILED_LOAD_API_KEY)

		if cls.MAILGUN_DOMAIN is None:
			raise MailGunException(FAILED_LOAD_DOMAIN)

		response = post(
			f"http://api.mailgun.net/v3/{cls.MAILGUN_DOMAIN}/messages",
			auth=("api", cls.MAILGUN_API_KEY),
			data={
				"from": f"{cls.FROM_TITLE} <{cls.FROM_EMAIL}>",
				"to": email,
				"subject": subject,
				"text": text,
				"html": html
			}
		)

		if response.status_code != 200:
			raise MailGunException(ERROR_SENDING_EMAIL)

		return response

