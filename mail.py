# doing necessary imports

import os
import smtplib
from email.message import EmailMessage
import logger


class mailer:
    """
    It is used as mailer

    Parameters
    ----------

    """

    def __init__(self):
        self.logger = logger.App_Logger("static/imagescrapper.log")  # creating App_Logger object
        self.logger.log("info", "Mailer object created")  # logging

    def mail(
        self,
        reciver_mail,
        subject="Image Scraper",
        title="Image Scraper",
        text="",
        link="",
    ):
        """
        It is used as mailer

        Parameters
        ----------
        reciver_mail: Reciver
        subject: mail subject
        title: title
        text: Mail text
        link: Link

        """
        EMAIL_ADDRESS = "testpyap@gmail.com"
        EMAIL_PASSWORD = os.environ['MPASS']
        print(EMAIL_PASSWORD)

        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = reciver_mail
            msg.set_content(
                text
                + """ 
            Thanks for your generosity!  """
            )

            msg.add_alternative(
                """<div data-marker="__QUOTED_TEXT__">
<div>
<div style="font-family: arial, helvetica, sans-serif; font-size: 12pt; color: #000000;">
<div style="font-family: arial, helvetica, sans-serif; font-size: 12pt; color: #000000;">
<div dir="auto"></div>
<br /><u></u>
<div style="margin: 0px; padding: 0px; background-color: #ffffff;">
<table style="border-collapse: collapse; table-layout: fixed; border-spacing: 0px; vertical-align: top; min-width: 320px; margin: 0px auto; background-color: #ffffff; width: 100%;" cellpadding="0" cellspacing="0">
<tbody>
<tr style="vertical-align: top;">
<td style="word-break: break-word; vertical-align: top; border-collapse: collapse !important;">
<div class="m_154136939071655347u-row-container" style="padding: 0px; background-color: transparent;">
<div style="margin: 0px auto; min-width: 320px; max-width: 600px; overflow-wrap: break-word; word-break: break-word; background-color: #9bc7eb;" class="m_154136939071655347u-row">
<div style="border-collapse: collapse; display: table; width: 100%; background-color: #9bc7eb;">
<div class="m_154136939071655347u-col m_154136939071655347u-col-100" style="max-width: 320px; min-width: 600px; display: table-cell; vertical-align: top;">
<div style="width: 100% !important;">
<div style="padding: 0px; border: 0px solid transparent;">
<table id="m_154136939071655347u_content_image_1" style="font-family: 'source sans pro', sans-serif;" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="word-break: break-word; padding: 40px 10px 19px; font-family: 'source sans pro', sans-serif;" align="left">
<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tbody>
<tr>
<td style="padding-right: 0px; padding-left: 0px;" align="center"><img align="center" border="0" alt="logo" title="logo" style="outline: none; text-decoration: none; clear: both; border: none; height: auto; float: none; width: 26%; max-width: 150.8px; display: block;" width="150.8" class="m_154136939071655347v-src-width m_154136939071655347v-src-max-width" dfsrc="https://ineuron.ai/assets/frontend/img/logo.png" src="https://ineuron.ai/assets/frontend/img/logo.png" saveddisplaymode="block" /></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
<table id="m_154136939071655347u_content_text_1" style="font-family: 'source sans pro', sans-serif;" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="word-break: break-word; padding: 10px 10px 0px; font-family: 'source sans pro', sans-serif;" align="left">
<div style="color: #363636; line-height: 140%; text-align: center; overflow-wrap: break-word;">
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 28px; line-height: 39.2px; color: #000080;"><strong><span style="line-height: 39.2px; font-size: 28px;">"""
                + title
                + """</span></strong></span></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="m_154136939071655347u-row-container" style="padding: 0px; background-color: transparent;">
<div style="margin: 0px auto; min-width: 320px; max-width: 600px; overflow-wrap: break-word; word-break: break-word; background-color: #f9f9f9;" class="m_154136939071655347u-row">
<div style="border-collapse: collapse; display: table; width: 100%; background-color: #f9f9f9;">
<div class="m_154136939071655347u-col m_154136939071655347u-col-100" style="max-width: 320px; min-width: 600px; display: table-cell; vertical-align: top;">
<div style="width: 100% !important;">
<div style="padding: 0px; border: 0px solid transparent;">
<table id="m_154136939071655347u_content_text_3" style="font-family: 'source sans pro', sans-serif;" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="word-break: break-word; padding: 28px 33px 11px; font-family: 'source sans pro', sans-serif;" align="left">
<div style="color: #444444; line-height: 200%; text-align: center; overflow-wrap: break-word;">
<div style="color: #444444; line-height: 200%; text-align: center; overflow-wrap: break-word;">
<p style="font-size: 14px; line-height: 200%;"><span></span><br /><span style="font-size: 16px; line-height: 32px;"></span></p>
<p></p>
<p><span style="font-size: 16pt;">"""
                + text
                + '''</span></p>
</div>
</div>
<div style="line-height: 200%; text-align: center; overflow-wrap: break-word;">
<p style="color: #444444;"><span style="font-size: 10pt;"><a href="'''
                + link
                + """">"""
                + link
                + """</a></span></p>
<div style="clear: both;"></div>
<p style="color: #444444;"></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="m_154136939071655347u-row-container" style="padding: 0px; background-color: transparent;">
<div style="margin: 0px auto; min-width: 320px; max-width: 600px; overflow-wrap: break-word; word-break: break-word; background-color: #f9f9f9;" class="m_154136939071655347u-row">
<div style="border-collapse: collapse; display: table; width: 100%; background-color: #f9f9f9;">
<div class="m_154136939071655347u-col m_154136939071655347u-col-100" style="max-width: 320px; min-width: 600px; display: table-cell; vertical-align: top;">
<div style="width: 100% !important;">
<div style="padding: 0px; border: 0px solid transparent;">
<table id="m_154136939071655347u_content_divider_1" style="font-family: 'source sans pro', sans-serif;" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="word-break: break-word; padding: 18px; font-family: 'source sans pro', sans-serif;" align="left">
<table align="center" border="0" cellpadding="0" cellspacing="0" width="84%" style="border-collapse: collapse; table-layout: fixed; border-spacing: 0px; vertical-align: top; border-top: 1px solid #d8d0d0;">
<tbody>
<tr style="vertical-align: top;">
<td style="word-break: break-word; vertical-align: top; font-size: 0px; line-height: 0px; border-collapse: collapse !important;"><span>&nbsp;</span></td>
</tr>
</tbody>
</table>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="m_154136939071655347u-row-container" style="padding: 0px; background-color: transparent;">
<div style="margin: 0px auto; min-width: 320px; max-width: 600px; overflow-wrap: break-word; word-break: break-word; background-color: #f9f9f9;" class="m_154136939071655347u-row">
<div style="border-collapse: collapse; display: table; width: 100%; background-color: #f9f9f9;">
<div class="m_154136939071655347u-col m_154136939071655347u-col-100" style="max-width: 320px; min-width: 600px; display: table-cell; vertical-align: top;">
<div style="width: 100% !important;">
<div style="padding: 0px; border: 0px solid transparent;">
<table id="m_154136939071655347u_content_text_2" style="font-family: 'source sans pro', sans-serif;" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="word-break: break-word; padding: 0px 33px 20px; font-family: 'source sans pro', sans-serif;" align="left">
<div style="color: #272362; line-height: 140%; text-align: center; overflow-wrap: break-word;">
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 24px; line-height: 33.6px;">Have a nice day.</span></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="m_154136939071655347u-row-container" style="padding: 0px; background-color: transparent;">
<div style="margin: 0px auto; min-width: 320px; max-width: 600px; overflow-wrap: break-word; word-break: break-word; background-color: #272362;" class="m_154136939071655347u-row">
<div style="border-collapse: collapse; display: table; width: 100%; background-color: #272362;">
<div class="m_154136939071655347u-col m_154136939071655347u-col-100" style="max-width: 320px; min-width: 600px; display: table-cell; vertical-align: top;">
<div style="width: 100% !important;">
<div style="padding: 0px; border: 0px solid transparent;">
<table id="m_154136939071655347u_content_text_6" style="font-family: 'source sans pro', sans-serif;" cellpadding="0" cellspacing="0" width="100%" border="0">
<tbody>
<tr>
<td style="word-break: break-word; padding: 15px 40px; font-family: 'source sans pro', sans-serif;" align="left">
<div style="color: #bbbbbb; line-height: 140%; text-align: center; overflow-wrap: break-word;">
<p style="font-size: 14px; line-height: 140%;"><span style="font-size: 12px; line-height: 16.8px;">&copy; Copyright <span style="text-decoration: underline; font-size: 12px; line-height: 16.8px;"><span style="color: #bbbbbb; font-size: 12px; line-height: 16.8px; text-decoration: underline;"><a style="color: #bbbbbb; text-decoration: underline;" href="https://u18335719.ct.sendgrid.net/ls/click?upn=pBJZFEzKP6j0HowC1qsv0nNtydwY76jGRLruA7mG9SY-3DNGGV_6OSwpf9XJOdfl3vGHPGpIykzR0beeGfWXy-2BK7N1m7UhSK3IpBGZzvgG6EPtU2xzyM7tWUdvWII66ew6Iq2xUQgZSn9kR8GHK43x4Y2-2BImvhu5rp01UP9FFIK87pi-2FvfFZ7qwH14g1lyiuU4RGGxzMfKgBfBJhJbVOwduDCPwt-2BAyaBn45PUPiKt6ZtO-2FsdPTy1Kq4xkjtg2GJXOhdIv5KSZyuZ-2B3HfA0fncaQh-2BE7Gs-3D" rel="noopener noreferrer" target="_blank">iNeuron.ai</a></span></span> Pvt. Ltd. All rights reserved</span></p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>""",
                subtype="html",
            )

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)

            self.logger.log("info", "Mail sent = " + reciver_mail)
            return True
        except Exception as e:
            self.logger.log("error", "Mail not sent = " + reciver_mail + "," + str(e))
            return False
