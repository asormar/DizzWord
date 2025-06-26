import reflex as rx

config = rx.Config(
    app_name="DizzWord",
    api_url="https://dizzword.up.railway.app",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)