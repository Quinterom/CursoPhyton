import flet as ft

def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Introduce tu nombre"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hola, {name}!"))

    txt_name = ft.TextField(label="Tu nombre")

    page.add(txt_name, ft.ElevatedButton("Saludar!!!", on_click=btn_click))

ft.app(target=main)