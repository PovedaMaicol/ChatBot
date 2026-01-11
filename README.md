# 🧠 English Tutor AI – Full Stack Chatbot

Un chatbot tutor de inglés construido con **FastAPI + Transformers en el backend y Next.js en el frontend.**
El tutor puede recordar información básica del estudiante (como su nombre o país) durante la conversación y responder siempre en inglés.

Este proyecto está pensado como portafolio profesional, siguiendo buenas prácticas de arquitectura y separación de responsabilidades.

## 🚀 Demo (local)

* Backend: http://localhost:8000

* Swagger UI: http://localhost:8000/docs

* Frontend: http://localhost:3000

# 🏗️ Arquitectura (Monorepo)
```
chatbot/
│
├── backend/
│   ├── app/
│   │   ├── main.py        # FastAPI entrypoint
│   │   ├── tutor.py       # Core logic (prompt + model)
│   │   ├── memory.py      # Session memory handling
│   │   ├── schemas.py     # Pydantic models
│   │
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── app/
│   │   └── page.tsx       # Chat UI (Next.js App Router)
│   ├── package.json
│   └── README.md
│
└── README.md              # (este archivo)
```

# 🧠 Características principales

✅ Tutor de inglés basado en FLAN-T5

✅ Respuestas siempre en inglés

✅ Corrección breve de errores gramaticales

✅ Memoria simple por sesión (session_id)

✅ API REST con FastAPI

✅ UI moderna con Next.js + Tailwind

✅ Arquitectura escalable (lista para DB / auth)

# 🧩 Backend – FastAPI
**Tecnologías**

Python

FastAPI

HuggingFace Transformers

Pydantic

Uvicorn

**Instalación**

cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

**Ejecutar servidor**

uvicorn app.main:app --reload

Endpoint principal

**POST /chat**

```
Request
{
  "message": "my name is maicol",
  "session_id": "uuid"
}

Response
{
  "reply": "Nice to meet you, Maicol!",
  "memory": {
    "name": "Maicol",
    "country": null
  }
}
```

# 🎨 Frontend – Next.js
**Tecnologías**

Next.js (App Router)

TypeScript

Tailwind CSS

Fetch API

**Instalación**
cd frontend
npm install
npm run dev

**Funcionalidades**

Chat en tiempo real

Persistencia de sesión con localStorage

Indicador de escritura

UI limpia y responsive

# 🧠 Memoria de sesión

Cada usuario recibe un session_id único que se guarda en el navegador.
Esto permite que el tutor recuerde información básica durante la conversación.

En el futuro, esta memoria puede migrarse fácilmente a:

Base de datos

Redis

Autenticación por usuario

🔮 Próximas mejoras

🔐 Autenticación de usuarios

🗄️ Persistencia en base de datos

⚡ Streaming de respuestas

🌍 Deploy (Vercel + Railway / Render)

🧠 Mejora de prompts y fine-tuning

👨‍💻 Autor

Maicol Salazar
Full Stack Developer

GitHub: https://github.com/PovedaMaicol

Proyecto pensado como parte de portafolio profesional

📄 Licencia

MIT License
