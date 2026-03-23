import flet as ft
from home_view import home_view
# from log import log_view
# from shop import shop_view

def main(page: ft.Page):

    def route_change(route):
        page.views.clear()

        if page.route == "/":
            page.views.append(home_view(page))

        # elif page.route == "/log":
        #     page.views.append(log_view(page))

        # elif page.route == "/shop":
        #     page.views.append(shop_view(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    page.go("/")


if __name__ == "__main__":
    import webbrowser, os
    if os.getenv("FLET_NO_BROWSER"):
        webbrowser.open = lambda *args, **kwargs: None
    ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)