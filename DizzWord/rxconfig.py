import reflex as rx

config = rx.Config(
    app_name="DizzWord",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ],
)