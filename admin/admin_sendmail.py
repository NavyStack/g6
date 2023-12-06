import math
from fastapi import APIRouter, Depends, Query, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy import asc, desc, and_, or_, func, extract
from sqlalchemy.orm import Session
from common.database import db_session, engine
import common.models as models 
from lib.common import *
from fastapi import FastAPI, HTTPException
import ssl
import os
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

from lib.plugin.service import get_admin_plugin_menus, get_all_plugin_module_names

router = APIRouter()
templates = AdminTemplates()
templates.env.globals['getattr'] = getattr
templates.env.globals['get_selected'] = get_selected
templates.env.globals['option_selected'] = option_selected
templates.env.globals['get_skin_select'] = get_skin_select
templates.env.globals['get_group_select'] = get_group_select
templates.env.globals['get_editor_select'] = get_editor_select
templates.env.globals['get_member_level_select'] = get_member_level_select
templates.env.globals['subject_sort_link'] = subject_sort_link
templates.env.globals['get_admin_menus'] = get_admin_menus
templates.env.globals["get_admin_plugin_menus"] = get_admin_plugin_menus
templates.env.globals["get_all_plugin_module_names"] = get_all_plugin_module_names
templates.env.globals["domain_mail_host"] = domain_mail_host


@router.get("/sendmail_test")
async def visit_search(request: Request, db: db_session,
        ):
    '''
    메일 테스트
    '''
    request.session["menu_key"] = "100300"
    
    context = {
        "request": request,
        "config": request.state.config,
        "member": request.state.login_member,
    }
    return templates.TemplateResponse("sendmail_test.html", context)


@router.post("/sendmail_test_result")
async def sendmail_test_result(request: Request, db: db_session,
        token: str = Form(..., alias="token"),
        to_email: str = Form(..., alias="email"),
        ):
    '''
    메일 테스트 실행
    '''
    if not check_token(request, token):
        raise AlertException("잘못된 접근입니다.")

    # ','를 기준으로 문자열을 분리하여 리스트로 변환하거나, 하나의 요소만 있는 리스트를 생성
    subject = "[메일검사] 제목"
    body = f'<span style="font-size:9pt;">[메일검사] 내용<p>이 내용이 제대로 보인다면 보내는 메일 서버에는 이상이 없는것입니다.<p>{datetime.now()}<p>이 메일 주소로는 회신되지 않습니다.</span>'
    
    mailer(to_email, subject, body)

    real_emails = to_email.split(',') if ',' in to_email else [to_email]
    
    context = {
        "request": request,
        "config": request.state.config,
        "member": request.state.login_member,
        "real_emails": real_emails,
    }
    return templates.TemplateResponse("sendmail_test_result.html", context)

# load_dotenv()

# SMTP_SERVER = os.getenv("SMTP_SERVER")
# SMTP_PORT = os.getenv("SMTP_PORT")
# SMTP_USERNAME = os.getenv("SMTP_USERNAME")
# SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

# def mailer_thread(to_email: str, subject: str, body: str):
    
#     try:
#         msg = MIMEMultipart()
#         msg['From'] = SMTP_USERNAME
#         msg['To'] = to_email
#         msg['Subject'] = subject

#         msg.attach(MIMEText(body, 'html')) # 텍스트는 plain

#         with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#             if SMTP_USERNAME and SMTP_PASSWORD:
#                 server.starttls()
#                 server.login(SMTP_USERNAME, SMTP_PASSWORD)
#             text = msg.as_string()
#             server.sendmail(SMTP_USERNAME, to_email, text)

#     except Exception as e:
#         print(f"Error sending email to {to_email}: {e}")

# def mailer(to_emails: List[str], subject: str, body: str):
#     threads = []

#     for to_email in to_emails:
#         thread = threading.Thread(target=mailer_thread, args=(to_email, subject, body))
#         threads.append(thread)
#         thread.start()

#     for thread in threads:
#         thread.join()

#     return {"message": f"Emails sent successfully to {', '.join(to_emails)}"}

# common.py 에서 사용
# def mailer(to_emails: List[str], subject: str, body: str):
#     for to_email in to_emails:
#         try:
#             msg = MIMEMultipart()
#             msg['From'] = SMTP_USERNAME
#             msg['To'] = to_email
#             msg['Subject'] = subject
            
#             # Assuming body is HTML, if not change 'html' to 'plain'
#             msg.attach(MIMEText(body, 'html'))  

#             with smtplib.SMTP(SMTP_SERVER, int(SMTP_PORT)) as server:
#                 if SMTP_USERNAME and SMTP_PASSWORD:
#                     server.starttls()
#                     server.login(SMTP_USERNAME, SMTP_PASSWORD)
#                 text = msg.as_string()
#                 server.sendmail(SMTP_USERNAME, to_email, text)

#         except Exception as e:
#             print(f"Error sending email to {to_email}: {e}")

#     return {"message": f"Emails sent successfully to {', '.join(to_emails)}"}                