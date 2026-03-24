import asyncio
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
                        ft.Row(
                            controls=
                            [
                                ft.Text("츄츄(4년 9개월,♀)", size=20, color=ft.Colors.BLACK_54),
                            ]
                        ),
                        ft.Container(
                            alignment=ft.Alignment(1, 0),
                            content=ft.IconButton(icon=ft.Icons.NOTIFICATIONS_OUTLINED, icon_color=ft.Colors.BROWN_300, icon_size=30),
                            # ft.IconButton(icon=ft.Icons.SETTINGS_OUTLINED, icon_color=ft.Colors.BROWN_300, icon_size=25),
                        ),
                    ],
                    alignment=align,
                ),
                bgcolor=ft.Colors.YELLOW_500,
            ),
        ],
    )


def main(page: ft.Page):
    def change_page(event):
        print(event)
        idx = event.control.selected_index

        if idx == 0:
            asyncio.create_task(page.push_route("/"))
        elif idx == 1:
            asyncio.create_task(page.push_route("/log"))
        elif idx == 2:
            asyncio.create_task(page.push_route("/shop"))
        elif idx == 3:
            asyncio.create_task(page.push_route("/contents"))
        elif idx == 4:
            asyncio.create_task(page.push_route("/mypage"))

    def bottom_nav():
        return ft.CupertinoNavigationBar(
            bgcolor=ft.Colors.YELLOW_500,
            inactive_color=ft.Colors.BROWN_200,
            active_color=ft.Colors.BROWN_700,
            on_change= lambda e : change_page(e),

            destinations=[
                ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                ft.NavigationBarDestination(icon=ft.Icons.CALENDAR_MONTH, label="Log"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.FOOD_BANK_ROUNDED,
                    selected_icon=ft.Icons.SHOPPING_CART,
                    label="Shop",
                ),
                ft.NavigationBarDestination(icon=ft.Icons.MESSENGER_OUTLINE_ROUNDED, label="Contents"),
                ft.NavigationBarDestination(
                    icon=ft.Icons.PERSON_OUTLINE,
                    selected_icon=ft.Icons.PERSON,
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
        
        else:
            return ft.Text('페이지 준비 중')

    def route_change(e):
        print('1')
        page.views.clear()

        body = get_body()

        page.views.append(
            ft.View(
                route=page.route,
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

    page.on_route_change = route_change #페이지 이동 감지 시 실행
    # asyncio.create_task(page.push_route("/"))

    page.route = "/"
    route_change(None)

if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.run(
        main,
        assets_dir="assets",
        view=ft.AppView.WEB_BROWSER,
        port=34636,
    )