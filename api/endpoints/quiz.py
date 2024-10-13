from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from quiz_model import QuizResponse
from PythonBackend.services.quiz_service import evaluate_quiz, get_next_module
#from api.endpoints.auth_service import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

router = APIRouter()

@router.post("/submit_quiz")
def submit_quiz(response: QuizResponse, token: str = Depends(oauth2_scheme)):
    user = token  # Implementa esta función para obtener el usuario desde el token
    if not user:
        raise HTTPException(status_code=401, detail="Not authenticated")

    analysis = evaluate_quiz(response, user.email)  # Asocia el resultado con el email del usuario
    if analysis["pass"]:
        next_module = get_next_module(user.email)
        return {"message": f"Has desbloqueado el módulo {next_module}", "next_module": next_module}
    else:
        return {"message": "Revisa el contenido y vuelve a intentarlo."}
