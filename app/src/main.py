import flet as ft
from home import home_view
from log import log_view
# from shop import shop_view

# 상단
def top_bar(align: ft.MainAxisAlignment):
    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Row(
                    [
                        ft.Container(
                            width=50,
                            height=50,
                        ),
                        ft.Icon(
                            ft.Icons.PETS,
                            size=30,
                            color=ft.Colors.BROWN_700
                        ),
                        # ft.Text("🐾똑똑🐾", size=24, weight=ft.FontWeight.BOLD, color=ft.Colors.BROWN_700),
                        # ft.IconButton(
                        #     icon=ft.Icons.SETTINGS,
                        #     icon_color=ft.Colors.BROWN_300,
                        #     icon_size=30
                        # )
                        ft.Row(controls=[
                            ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=ft.Colors.BROWN_300, icon_size=25),
                            ft.IconButton(icon=ft.Icons.SETTINGS_OUTLINED, icon_color=ft.Colors.BROWN_300, icon_size=25),
                        ], spacing=0),
                    ],
                    alignment=align,
                    # width=360,   # 추가
                ),
                bgcolor=ft.Colors.YELLOW,
                # width=360,      # 추가
            ),
        ],
    )


def main(page: ft.Page):
    # page.bgcolor = ft.Colors.YELLOW
    
    def change_page(event):
        print(event)
        idx = event.control.selected_index

        if idx == 0:
            page.go('/')
        elif idx == 1:
            page.go('/log')
        elif idx == 1:
            page.go('/shop')
        elif idx == 1:
            page.go('/AI')
        elif idx == 1:
            page.go('/MyPage')


    def bottom_nav():
        return ft.CupertinoNavigationBar(
            bgcolor=ft.Colors.YELLOW,
            inactive_color=ft.Colors.BROWN_200,
            active_color=ft.Colors.BROWN_700,
            on_change= lambda e : change_page(e),

            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.SHOP,
                    selected_icon=ft.Icons.SHOPPING_CART,
                    label="Shop",
                ),
                ft.NavigationBarDestination(icon=ft.Icons.STAR, label="AI"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.DOOR_FRONT_DOOR,
                    selected_icon=ft.Icons.DOOR_BACK_DOOR_OUTLINED,
                    label="MyPage"
                ),
            ],
        ) 

    def get_body():
        if page.route == "/":
            return home_view(page)

        elif page.route == "/log":
            return log_view(page)

        # elif page.route == "/shop":
        #     page.views.append(shop_view(page))

    def route_change(route):
        page.views.clear()

        body = get_body()

        page.views.append(
            ft.View(
                route='/',
                # bgcolor=ft.Colors.YELLOW,
                navigation_bar=bottom_nav(),
                controls = [
                    top_bar(ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Container(
                        expand=True,
                        content=body,
                        padding=ft.padding.only(top=10, bottom=10),
                    )
                ],
                spacing=15,
            )
        )

        page.update()

    page.on_route_change = route_change
    page.go("/")


if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)