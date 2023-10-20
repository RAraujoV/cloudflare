import flet as ft
def main(page: ft.Page):
    page.title = "Flet Hello"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    dlg = ft.AlertDialog(
        title=ft.Text("Hola")
    )

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    page.appbar = ft.AppBar(
        title=ft.Text("Hello Word...")
    )
    page.add(
        ft.Row(
            [
                ft.Text("Hello world"),
                ft.ElevatedButton(text = "Show hello world",on_click=open_dlg)
            ]
        )      
    )
ft.app(target=main)
