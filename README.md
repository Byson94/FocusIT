# FocusIT <img src="https://github.com/user-attachments/assets/4112b67c-3762-4ec0-a879-6b55cb5d889f" width="25" height="25" style="border-radius: 8px;">


![image](https://github.com/user-attachments/assets/214122d2-4af5-4a78-aee3-24180cdb2b82)


Focusit is a simple program to keep track of the time you spend on a task and analyze your weekly performance on the tasks you did.

> NOTE: This program can be used only on unix based systems. If you use windows, the code will not work on your system.

## Download the program:

Run the following command to clone the repository to your system (you can install repository as .zip if you want to)

```bash
git clone https://github.com/Byson94/FocusIT
```

## Prerequisites

Make sure that you have the prerequisites to run the program or else it will not work.

- **Prerequisites**
  - **rich**
  - **appdirs**

**Run the following command to install the prerequisites.**

```bash
pip install -r requirements.txt
```

## Notes

- If you are running this program locally, then make sure to run `python -m venv ./venv` to setup a virtual enviornment to install the prerequisites to.

- If you want to run this program globally, then running the following command will make it globally accessable by calling `focusit` (make sure that the prerequisites are installed to your system to make it run)

```bash
sudo cp main.py /usr/local/bin/focusit
```

After running that, run the following code so that you can call it without any permission issues.

```bash
sudo chmod +x /usr/local/bin/focusit
```

- The above commands copies the python script and gives it permission to execute aswell as making it trigger when focusit is triggered.
