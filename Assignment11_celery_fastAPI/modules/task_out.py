from typing import Union
from pydantic import BaseModel
from celery.result import AsyncResult


class TaskOut(BaseModel):
    id: str
    status: str
    result: Union[str,None]

def _to_taskout(r: AsyncResult) -> TaskOut:
    return TaskOut(
        id=r.task_id, 
        status=r.status, 
        result=r.traceback if r.failed() else r.result,
    )