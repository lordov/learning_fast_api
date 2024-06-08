from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException

from src.auth.base_config import auth_backend, fastapi_users, current_user

from src.tasks.tasks import send_email_report_dashboard


router = APIRouter(prefix="/report", tags=["Report"])


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {
        'status': 200,
        'data': 'Email sent',
        'details': None
    }
