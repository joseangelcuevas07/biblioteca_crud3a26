import flet as ft 

def main_window(page: ft.Page):
    page.title = "Sistema de biblioteca universitaria"
    page.window_width = 1100
    page.windown_height = 700
    page.padding = 0
    page.bgcolor = "#f5f5f5"
    page.bgcolor = ft.Colors.BLUE_GREY_50
    
    #ejemplo de widget
    titulo = ft.Text(
        "Sistema de Biblioteca Universiatria",
        size=24,
        weight=ft.FontWeight.BOLD
        )
    
    subtitulo = ft.Text(
        "Seleccione una opción del menú",
        size=16,
        color = ft.Colors.BLUE_GREY_600
    )
    
    #widget Container
    contenido = ft.Container(
        content = ft.Column(
            controls=[
                titulo,
                subtitulo
            ],
            spacing=10
        ),
        padding=30,                      
        expand=True
    )
    
    menu_lateral = ft.Container(
        width=220,
        bgcolor= ft.Colors.BLUE_GREY_900,
        padding=20,
        content= ft.Column(
            controls= [
                ft.Text(
                    "Biblioteca",
                    size= 22,
                    weight= ft.FontWeight.BOLD,
                    color= ft.Colors.WHITE
                ),
                ft.Text(
                    "Sistema de gestión",
                    size= 12,
                    color= ft.Colors.BLUE_GREY_100
                ),
                ft.Divider(color = ft.Colors.BLUE_GREY_700),
                ft.ElevatedButton(
                    text = "Libros",
                    icon = ft.Icons.BOOK,
                    widht = 180,
                    
                ),
                ft.ElevatedButton(
                    text = "Usuarios",
                    icon = ft.Icons.PERSON,
                    widht = 180,
                    
                ),
                ft.ElevatedButton(
                    text = "Prestamos",
                    icon = ft.Icons.SWAP_HORIZ,
                    widht = 180,
                    
                ),
                ft.ElevatedButton(
                    text = "Devoluciones",
                    icon = ft.Icons.KEYBOARD_RETURN,
                    widht = 180,
                    
                ),                
            ],
            spacing= 15
            
        )
    )
    
    layout = ft.Row(
        controls= [
            menu_lateral,
            contenido
        ],
        expand = True
    )
    
    page.add(layout)