import keyboard
import time
import psutil

def stop_game():
    for proc in psutil.process_iter(['pid', 'name']):
        if name in proc.info['name']:
            print(f"Зупинено процес гри з PID: {proc.info['pid']}")
            proc.suspend()

def resume_game():
    for proc in psutil.process_iter(['pid', 'name']):
        if name in proc.info['name']:
            print(f"Відновлено процес гри з PID: {proc.info['pid']}")
            proc.resume()



# Встановлюємо гарячі клавіші для зупинки та продовження гри
keyboard.add_hotkey('ctrl+alt+p', stop_game)
keyboard.add_hotkey('ctrl+alt+r', resume_game)

if __name__ == '__main--':

    name = 'Albion'

    try:
        while True:
            time.sleep(1)  # Затримка для уникнення споживання великої кількості CPU
    except KeyboardInterrupt:
        print("Програма завершила роботу.")