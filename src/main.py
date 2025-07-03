import flet as ft
import random

def main(page: ft.Page):
    page.title = "Number Guessing Game"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_width = 400
    page.window_height = 500
    #page.scroll= 'always'
    page.window_resizable = False
    page.bgcolor = ft.Colors.TRANSPARENT
    page.decoration = ft.BoxDecoration(
        image= ft.DecorationImage(
            src="https://images.unsplash.com/photo-1557682250-33bd709cbe85?w=900&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cHVycGxlJTIwZ3JhZGllbnR8ZW58MHx8MHx8fDA%3D",
            fit= ft.ImageFit.COVER,
        )
    )


    page.fonts = {
        "SpaceMission": "fonts/SpaceMission-rgyw9.otf",
        "Uncracked":"fonts/Uncracked-X3Wjk.otf"
    }
    # Game state variables
    secret_number = random.randint(1, 100)
    attempts = 0
    print ("-->", secret_number)

    # UI elements
    title_text = ft.Text(
        "Guess the Number!🎲",
        size=45,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLACK,
        font_family="SpaceMission"
    )

    instructions_text = ft.Text(
        "Can you guess the secret number between 1 and 100 ?",
        size=16,
        color=ft.Colors.BLACK
    )

    guess_input = ft.TextField(
        label="Enter your guess",
        hint_text="1-100",
        keyboard_type=ft.KeyboardType.NUMBER,
        text_align=ft.TextAlign.CENTER,
        width=200,
        border_radius=10,
        border_color=ft.Colors.BLACK,
        focused_border_color=ft.Colors.WHITE
    )

    feedback_text = ft.Text(
        "",
        size=30,
        weight=ft.FontWeight.NORMAL, # Changed from MEDIUM to NORMAL
        color=ft.Colors.BLUE_GREY_500,
        font_family="Uncracked"
    )

    attempts_text = ft.Text(
        "Attempts: 0",
        size=14,
        weight=ft.FontWeight.NORMAL, # Changed from MEDIUM to NORMAL
        color=ft.Colors.BLACK
    )
    rules_card = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("📋 Game Rules", size=16, weight=ft.FontWeight.BOLD),
                ft.Text("• Guess a number between 1 and 100", size=14),
                #ft.Text("• You have 7 attempts to find it", size=14),
                ft.Text("• I'll give you hints along the way", size=14),
                ft.Text("• Good luck!! 🍀", size=14, weight=ft.FontWeight.W_500),
            ], spacing=5),
            padding=15
        ),
        elevation=2
    )
    
    # Score/Stats card
    stats_card = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("📊 Current Game", size=16, weight=ft.FontWeight.BOLD),
                attempts_text,
                ft.Text("Range: 1 - 100", size=14, color=ft.Colors.GREY_600),
            ], spacing=5),
            padding=15
        ),
        elevation=2
    )
    

    def check_guess(e):
        nonlocal attempts, secret_number

        try:
            guess = int(guess_input.value)
            attempts += 1
            attempts_text.value = f"Attempts: {attempts}"

            

            if guess < 1 or guess > 100:
                feedback_text.value = "Please enter a number between 1 and 100."
                feedback_text.color = ft.Colors.RED_500
            elif guess < secret_number:
                feedback_text.value = "Too low! Try again."
                feedback_text.color = ft.Colors.ORANGE_700
            elif guess > secret_number:
                feedback_text.value = "Too high! Try again."
                feedback_text.color = ft.Colors.ORANGE_700
            else:
                feedback_text.value = f"Congratulations! You guessed it in {attempts} attempts!"
                feedback_text.color = ft.Colors.GREEN_700
                guess_input.disabled = True
                guess_button.disabled = True
                restart_button.visible = True

            guess_input.value = "" # Clear input after guess
            page.update()

        except ValueError:
            feedback_text.value = "Invalid input. Please enter a whole number."
            feedback_text.color = ft.Colors.RED_500
            page.update()

    def restart_game(e):
        nonlocal secret_number, attempts
        secret_number = random.randint(1, 100)
        attempts = 0
        attempts_text.value = "Attempts: 0"
        feedback_text.value = ""
        guess_input.value = ""
        guess_input.disabled = False
        guess_button.disabled = False
        restart_button.visible = False
        page.update()

    guess_button = ft.ElevatedButton(
        "Submit Guess",
        on_click=check_guess,
        icon=ft.Icons.SEND,
        bgcolor=ft.Colors.PURPLE,
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15
        )
    )

    restart_button = ft.OutlinedButton(
        "Play Again",
        on_click=restart_game,
        icon=ft.Icons.RESTART_ALT,
        visible=False, # Initially hidden
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=15,
            side=ft.BorderSide(2, ft.Colors.BLUE_600),
            color=ft.Colors.BLUE_600
        )
    )

    # Add controls to the page
    page.add(
        ft.Column(
            [
                title_text,
                instructions_text,
                ft.Container(height=20), # Spacer
                rules_card,
                ft.Container(height=20),
                guess_input,
                ft.Container(height=10), # Spacer
                guess_button,
                ft.Container(height=20), # Spacer
                feedback_text,
                attempts_text,
                ft.Container(height=20), # Spacer
                restart_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10
        )
    )

# Run the Flet application
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets")

    
