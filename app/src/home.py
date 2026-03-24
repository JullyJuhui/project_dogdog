import flet as ft


def home_view(page: ft.Page):
    image_dog = ft.Row(
        scroll=ft.ScrollMode.AUTO,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Row(
                [ft.Container(
                width=200,
                height=200,
                bgcolor=ft.Colors.BLACK,
                shape=ft.BoxShape.CIRCLE,
                image=ft.DecorationImage(
                    # src="https://pds.joongang.co.kr/news/component/htmlphoto_mmdata/201901/20/28017477-0365-4a43-b546-008b603da621.jpg",
                    src="대추.jpg",
                    # fit=ft.BoxFit.COVER,
                    fit=ft.ImageFit.COVER,
                ),
            ),],
                ft.Container(
                    ft.Text("대추")
                )
            ),
        ]
    )
    # image_dog.controls[0].width = 100

    button_style = ft.ButtonStyle(
                        shape=ft.RoundedRectangleBorder(radius=10),
                        bgcolor = ft.Colors.BROWN_400,
                        color = ft.Colors.AMBER_100
                    )
    
    status_dog = ft.Column(
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                width=360,
                spacing=8,
                controls=[
                    ft.Container(
                        # content=ft.Text("섭취량"),
                        content=ft.Column([
                        ft.Text("🦴", size=26),
                        ft.Text("섭취량", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.BROWN_700),
                    ], alignment="center", horizontal_alignment="center"),
                        padding=2,
                        # alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.AMBER_200,
                        width=115,
                        height=70,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Column([
                        ft.Text("💧", size=26),
                        ft.Text("음수량", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.BROWN_700),
                    ], alignment="center", horizontal_alignment="center"),
                        padding=2,
                        # alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.AMBER_200,
                        width=115,
                        height=70,
                        border_radius=10,
                    ),
                    ft.Container(
                        content=ft.Column([
                        ft.Text("사료잔량", size=12, weight=ft.FontWeight.W_600, color=ft.Colors.BROWN_700),
                    ], alignment="center", horizontal_alignment="center"),
                        padding=2,
                        # alignment=ft.Alignment.CENTER,
                        bgcolor=ft.Colors.AMBER_200,
                        width=115,
                        height=70,
                        border_radius=10,
                    ),
                ],
            ),
            ft.Container(
                ft.ElevatedButton(
                    "오늘 기록",
                    style=button_style
                ),
                    # alignment=ft.Alignment.CENTER,
                    # bgcolor=ft.Colors.AMBER_200,
                    width=290,
                    height=50,
                    border_radius=10,
                ),

        ]
    )
    
    input_button = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                    ft.Row(
                        [
                            ft.Button(
                                "밥주기",
                                style=button_style,
                                # alignment=ft.Alignment.CENTER,
                                # bgcolor=ft.Colors.AMBER_200,
                                width=90,
                                height=60,
                            ),
                        
                            ft.Button(
                                "물주기",
                                style=button_style,
                                # margin = 5,
                                # alignment=ft.Alignment.CENTER,
                                # bgcolor=ft.Colors.AMBER_200,
                                width=90,
                                height=60,
                            ),

                            ft.Button(
                                "건강",
                                style=button_style,
                                # alignment=ft.Alignment.CENTER,
                                # bgcolor=ft.Colors.AMBER_200,
                                width=90,
                                height=60,
                            ),    
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # 추가
                    ),
                    ft.Row(
                        [
                            ft.Button(
                                "활동",
                                style=button_style,
                                # alignment=ft.Alignment.CENTER,
                                # bgcolor=ft.Colors.AMBER_200,
                                width=90,
                                height=60,
                            ),
                            
                            ft.Button(
                                "위생",
                                style=button_style,
                                # alignment=ft.Alignment.CENTER,
                                # bgcolor=ft.Colors.AMBER_200,
                                width=90,
                                height=60,
                            ),

                            ft.Button(
                                "배변",
                                style=button_style,
                                # alignment=ft.Alignment.CENTER,
                                # bgcolor=ft.Colors.AMBER_200,
                                width=90,
                                height=60,
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # 추가
                    ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 추가
                )
            ),
        ]
    )

    return ft.Column(
        scroll=ft.ScrollMode.AUTO,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # 추가
        controls=[
            # 상단
            # row_with_alignment(ft.MainAxisAlignment.SPACE_BETWEEN),

            # 메인 컨테이너
            image_dog,
            status_dog,
            input_button,
        ],
        spacing=15,
    )



# if __name__ == "__main__":
#     import webbrowser, os
#     if os.getenv("FLET_NO_BROWSER"):
#         webbrowser.open = lambda *args, **kwargs: None
#     ft.app(target=main, assets_dir="assets", view=ft.AppView.WEB_BROWSER, port=34636)