import reflex as rx

config = rx.Config(
    app_name="DizzWord",
    api_url="https://dizzword.up.railway.app",
    cors_allowed_origins=[
        "https://dizz-word.vercel.app",
        "http://localhost:3000/"
    ],
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)