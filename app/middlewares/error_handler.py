from fastapi import Request
from fastapi.responses import JSONResponse
from app.models.generic import ResponseModel, ErrorModel
from fastapi.exceptions import HTTPException

async def global_exception_handler(request: Request, call_next):
    try:
        response = await call_next(request)

        if response.status_code >= 400:
            error_response = ResponseModel(
                success=False,
                error=ErrorModel(
                    code=response.status_code
                )
            )
            return JSONResponse(status_code=response.status_code, content=error_response.model_dump())

        return response  # Başarılıysa orijinal yanıtı döndür
    except HTTPException as exc:
        # FastAPI HTTPException durumunda özel ResponseModel ile yanıt veriyoruz
        error_response = ResponseModel(
            success=False,
            error=ErrorModel(
                code=exc.status_code,
                message=exc.detail,
                details=f"Error occurred at {request.url.path}"
            )
        )
        return JSONResponse(status_code=exc.status_code, content=error_response.dict())
    except Exception as exc:
        # Diğer tüm hatalar için ResponseModel ile 500 yanıtı döndürüyoruz
        error_response = ResponseModel(
            success=False,
            error=ErrorModel(
                code=500,
                message="Internal Server Error",
                details=str(exc)
            )
        )
        return JSONResponse(status_code=500, content=error_response.dict())
