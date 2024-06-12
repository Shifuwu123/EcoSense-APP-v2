import flet as ft
from fonts import load_custom_fonts

def main(page: ft.Page):
    load_custom_fonts()
    
    page.title = "EcoSense - Inicio de Sesión"
    page.bgcolor = ft.colors.GREEN_500

    # Cabecera con iconos
    header = ft.Row(
        controls=[
            ft.Image(src="assets/images/image_x2.svg", width=28.4, height=11.1),
            ft.Row(
                controls=[
                    ft.Image(src="assets/images/mobile_signal_x2.svg", width=17, height=10.7),
                    ft.Image(src="assets/images/wifi_2_x2.svg", width=15.3, height=11),
                    ft.Image(src="assets/images/battery_2_x2.svg", width=24.3, height=11.3),
                ],
                spacing=5,
            ),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    # Título y Descripción
    title = ft.Text(
        "EcoSense",
        color=ft.colors.WHITE,
        style=ft.TextStyle(font_family="Holtwood One SC", font_size=36)
    )
    description = ft.Text(
        "Invernadero Autónomo con sistema de monitoreo en tiempo real y control remoto. Cultiva tus plantas sin preocupaciones!",
        color=ft.colors.WHITE,
        style=ft.TextStyle(font_family="Inter", font_size=16),
        text_align=ft.TextAlign.CENTER
    )

    # Campos de Entrada
    email_input = ft.TextField(
        label="Email",
        placeholder="email@domain.com",
        bgcolor=ft.colors.GREY_300,
        border_radius=8,
        width=300,
    )
    password_input = ft.TextField(
        label="Contraseña",
        placeholder="***********",
        bgcolor=ft.colors.GREY_300,
        border_radius=8,
        width=300,
        password=True,
    )

    # Botones
    login_button = ft.ElevatedButton("Log In", color=ft.colors.WHITE, bgcolor=ft.colors.GREEN_500, border_radius=8)
    signup_button = ft.TextButton("Sign up", color=ft.colors.GREEN_500)

    # Contenedor principal
    content = ft.Column(
        controls=[
            header,
            ft.SizedBox(height=20),
            title,
            description,
            ft.SizedBox(height=40),
            email_input,
            ft.SizedBox(height=20),
            password_input,
            ft.SizedBox(height=20),
            login_button,
            ft.Row(
                controls=[
                    ft.Divider(),
                    ft.Text("or create account", color=ft.colors.GREY_500),
                    ft.Divider(),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            signup_button,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(ft.Container(content, padding=20))

ft.app(target=main)
