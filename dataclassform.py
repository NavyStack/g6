from dataclasses import dataclass
from typing import Optional, List
from fastapi import Form

@dataclass
class ConfigForm:
    cf_title: str = Form(...)
    cf_admin: Optional[str] = Form(default="")
    cf_admin_email: Optional[str] = Form(default="")
    cf_admin_email_name: Optional[str] = Form(default="")
    cf_use_point: Optional[int] = Form(default=0)
    cf_login_point: Optional[int] = Form(default=0)
    cf_memo_send_point: Optional[int] = Form(default=0)
    cf_cut_name: Optional[int] = Form(default=0)
    cf_nick_modify: Optional[int] = Form(default=0)
    cf_new_del: Optional[int] = Form(default=0)
    cf_memo_del: Optional[int] = Form(default=0)
    cf_visit_del: Optional[int] = Form(default=0)
    cf_popular_del: Optional[int] = Form(default=0)
    cf_login_minutes: Optional[int] = Form(default=0)
    cf_new_rows: Optional[int] = Form(default=0)
    cf_page_rows: Optional[int] = Form(default=0)
    cf_mobile_page_rows: Optional[int] = Form(default=0)
    cf_write_pages: Optional[int] = Form(default=0)
    cf_mobile_pages: Optional[int] = Form(default=0)
    cf_new_skin: Optional[str] = Form(default="")
    cf_search_skin: Optional[str] = Form(default="")
    cf_mobile_search_skin: Optional[str] = Form(default="")
    cf_connect_skin: Optional[str] = Form(default="")
    cf_mobile_connect_skin: Optional[str] = Form(default="")
    cf_faq_skin: Optional[str] = Form(default="")
    cf_mobile_faq_skin: Optional[str] = Form(default="")
    cf_editor: Optional[str] = Form(default="")
    cf_captcha: Optional[str] = Form(default="")
    cf_captcha_mp3: Optional[str] = Form(default="")
    cf_recaptcha_site_key: Optional[str] = Form(default="")
    cf_recaptcha_secret_key: Optional[str] = Form(default="")
    cf_use_copy_log: Optional[int] = Form(default=0)
    cf_point_term: Optional[int] = Form(default=0)
    cf_possible_ip: Optional[str] = Form(default="")
    cf_intercept_ip: Optional[str] = Form(default="")
    cf_analytics: Optional[str] = Form(default="")
    cf_add_meta: Optional[str] = Form(default="")
    cf_syndi_token: Optional[str] = Form(default="")
    cf_syndi_except: Optional[str] = Form(default="")
    cf_delay_sec: Optional[int] = Form(default=0)
    cf_link_target: Optional[str] = Form(default="")
    cf_read_point: Optional[int] = Form(default=0)
    cf_write_point: Optional[int] = Form(default=0)
    cf_comment_point: Optional[int] = Form(default=0)
    cf_download_point: Optional[int] = Form(default=0)
    cf_search_part: Optional[str] = Form(default="")
    cf_image_extension: Optional[str] = Form(default="")
    cf_flash_extension: Optional[str] = Form(default="")
    cf_movie_extension: Optional[str] = Form(default="")
    cf_filter: Optional[str] = Form(default="")
    cf_member_skin: Optional[str] = Form(default="")
    cf_mobile_member_skin: Optional[str] = Form(default="")
    cf_use_homepage: Optional[int] = Form(default=0)
    cf_req_homepage: Optional[int] = Form(default=0)
    cf_use_addr: Optional[int] = Form(default=0)
    cf_req_addr: Optional[int] = Form(default=0)
    cf_use_tel: Optional[int] = Form(default=0)
    cf_req_tel: Optional[int] = Form(default=0)
    cf_use_hp: Optional[int] = Form(default=0)
    cf_req_hp: Optional[int] = Form(default=0)
    cf_use_signature: Optional[int] = Form(default=0)
    cf_req_signature: Optional[int] = Form(default=0)
    cf_use_profile: Optional[int] = Form(default=0)
    cf_req_profile: Optional[int] = Form(default=0)
    cf_register_level: Optional[int] = Form(default=0)
    cf_register_point: Optional[int] = Form(default=0)
    cf_leave_day: Optional[int] = Form(default=0)
    cf_use_member_icon: Optional[int] = Form(default=0)
    cf_icon_level: Optional[int] = Form(default=0)
    cf_member_icon_size: Optional[int] = Form(default=0)
    cf_member_icon_width: Optional[int] = Form(default=0)
    cf_member_icon_height: Optional[int] = Form(default=0)
    cf_member_img_size: Optional[int] = Form(default=0)
    cf_member_img_width: Optional[int] = Form(default=0)
    cf_member_img_height: Optional[int] = Form(default=0)
    cf_use_recommend: Optional[int] = Form(default=0)
    cf_recommend_point: Optional[int] = Form(default=0)
    cf_prohibit_id: Optional[str] = Form(default="")
    cf_prohibit_email: Optional[str] = Form(default="")
    cf_stipulation: Optional[str] = Form(default="")
    cf_privacy: Optional[str] = Form(default="")
    cf_cert_use: Optional[int] = Form(default=0)
    cf_cert_find: Optional[int] = Form(default=0)
    cf_cert_simple: Optional[int] = Form(default=0)
    cf_cert_hp: Optional[int] = Form(default=0)
    cf_cert_ipin: Optional[int] = Form(default=0)
    cf_cert_kg_mid: Optional[str] = Form(default="")
    cf_cert_kg_cd: Optional[str] = Form(default="")
    cf_cert_kcb_cd: Optional[str] = Form(default="")
    cf_cert_kcp_cd: Optional[str] = Form(default="")
    cf_cert_limit: Optional[int] = Form(default=0)
    cf_cert_req: Optional[int] = Form(default=0)
    cf_bbs_rewrite: Optional[int] = Form(default=0)
    cf_email_use: Optional[int] = Form(default=0)
    cf_use_email_certify: Optional[int] = Form(default=0)
    cf_formmail_is_member: Optional[int] = Form(default=0)
    cf_email_wr_super_admin: Optional[int] = Form(default=0)
    cf_email_wr_group_admin: Optional[int] = Form(default=0)
    cf_email_wr_board_admin: Optional[int] = Form(default=0)
    cf_email_wr_write: Optional[int] = Form(default=0)
    cf_email_wr_comment_all: Optional[int] = Form(default=0)
    cf_email_mb_super_admin: Optional[int] = Form(default=0)
    cf_email_mb_member: Optional[int] = Form(default=0)
    cf_email_po_super_admin: Optional[int] = Form(default=0)
    cf_social_login_use: Optional[int] = Form(default=0)
    cf_social_servicelist: Optional[List[str]] = Form(default="", alias="cf_social_servicelist[]")
    # cf_social_servicelist: Optional[str] = Form(default="")
    cf_naver_clientid: Optional[str] = Form(default="")
    cf_naver_secret: Optional[str] = Form(default="")
    cf_facebook_appid: Optional[str] = Form(default="")
    cf_twitter_key: Optional[str] = Form(default="")
    cf_google_clientid: Optional[str] = Form(default="")
    cf_googl_shorturl_apikey: Optional[str] = Form(default="")
    cf_kakao_rest_key: Optional[str] = Form(default="")
    cf_kakao_js_apikey: Optional[str] = Form(default="")
    cf_payco_clientid: Optional[str] = Form(default="")
    cf_payco_secret: Optional[str] = Form(default="")
    cf_add_script: Optional[str] = Form(default="")
    cf_sms_use: Optional[str] = Form(default="")
    cf_sms_type: Optional[str] = Form(default="")
    cf_icode_id: Optional[str] = Form(default="")
    cf_icode_pw: Optional[str] = Form(default="")
    cf_icode_server_ip: Optional[str] = Form(default="")
    cf_icode_token_key: Optional[str] = Form(default="")
    cf_1_subj: Optional[str] = Form(default="")
    cf_1: Optional[str] = Form(default="")
    cf_2_subj: Optional[str] = Form(default="")
    cf_2: Optional[str] = Form(default="")
    cf_3_subj: Optional[str] = Form(default="")
    cf_3: Optional[str] = Form(default="")
    cf_4_subj: Optional[str] = Form(default="")
    cf_4: Optional[str] = Form(default="")
    cf_5_subj: Optional[str] = Form(default="")
    cf_5: Optional[str] = Form(default="")
    cf_6_subj: Optional[str] = Form(default="")
    cf_6: Optional[str] = Form(default="")
    cf_7_subj: Optional[str] = Form(default="")
    cf_7: Optional[str] = Form(default="")
    cf_8_subj: Optional[str] = Form(default="")
    cf_8: Optional[str] = Form(default="")
    cf_9_subj: Optional[str] = Form(default="")
    cf_9: Optional[str] = Form(default="")
    cf_10_subj: Optional[str] = Form(default="")
    cf_10: Optional[str] = Form(default="")