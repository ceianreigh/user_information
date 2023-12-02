import tkinter as tk


# confirmation
def confirm_data(
    first_name,
    middle_name,
    last_name,
    age,
    barangay,
    municipality,
    province,
    region,
    country,
):
    confirmation_window = tk.Toplevel()
    confirmation_window.title("Confirmation")
    fg = ("#FFFFFF",)
    bg = ("#181D31",)
    confirmation_window.geometry("500x300")

    confirmation_label = tk.Label(
        confirmation_window,
        text=f"Please confirm the following information:\n\n"
        f"Your name is {first_name} {middle_name} {last_name}.\n"
        f"You are {age} years old.\n"
        f"You live in Barangay {barangay}, {municipality}, {province}, \n Region {region}, {country}.",
        font=("Poppins", 12),
    )
    confirmation_label.pack()

    # confirm_button
    confirm_button = tk.Button(
        confirmation_window,
        text="Confirm",
        font=("Poppins Medium", 14),
        fg="#FFFFFF",
        bg="#181D31",
        command=lambda: show_popup(
            first_name,
            middle_name,
            last_name,
            age,
            barangay,
            municipality,
            province,
            region,
            country,
        ),
    )
    confirm_button.pack()

    # reject_button
    reject_button = tk.Button(
        confirmation_window,
        text="Reject",
        font=("Poppins Medium", 14),
        fg="#FFFFFF",
        bg="#181D31",
        command=lambda: edit_data(
            first_name,
            middle_name,
            last_name,
            age,
            barangay,
            municipality,
            province,
            region,
            country,
            confirmation_window,
        ),
    )
    reject_button.pack()


# editing_wrong_data
def edit_data(
    first_name,
    middle_name,
    last_name,
    age,
    barangay,
    municipality,
    province,
    region,
    country,
    confirmation_window,
):
    confirmation_window.destroy()
    enable_entry_fields()


def enable_entry_fields():
    for widget in frame.winfo_children():
        if isinstance(widget, tk.LabelFrame):
            for entry in widget.winfo_children():
                if isinstance(entry, tk.Entry):
                    entry.config(state="normal")


# results_popup
def show_popup(
    first_name,
    middle_name,
    last_name,
    age,
    barangay,
    municipality,
    province,
    region,
    country,
):
    message = f"Thank for filling up!\n\n Full Name: {first_name} {middle_name} {last_name}\n Age: {age} years old\n Address: Barangay {barangay}, {municipality}, {province}, Region {region}, {country}"
    tk.messagebox.showinfo("Submission successful", message)
    window.destroy()


# collection_of_entered_data
def submit_data():
    agreement = agreement_var.get()

    if agreement == "Agree":
        first_name = first_name_entry.get()
        middle_name = middle_name_entry.get()
        last_name = last_name_entry.get()
        if first_name and last_name:
            age = age_spinbox.get()
            barangay = barangay_entry.get()
            municipality = municipality_entry.get()
            province = province_entry.get()
            region = region_entry.get()
            country = country_entry.get()

            confirm_data(
                first_name,
                middle_name,
                last_name,
                age,
                barangay,
                municipality,
                province,
                region,
                country,
            )

        else:
            tk.messagebox.showwarning(
                title="Error", message="No first name and last name entered."
            )
    else:
        tk.messagebox.showwarning(
            title="Error",
            message="Check the agreement box if you agree that all the information you put are all correct.",
        )


window = tk.Tk()
window.title("User Background")
window.configure(bg="#181D31")
window.geometry("800x1000")

text = tk.Label(
    window,
    text="User Background",
    font=("Poppins Bold Italic", 30),
    fg="#FFFFFF",
    bg="#181D31",
)
text.pack()

frame = tk.Frame(window)
frame.pack()

# name_and_age
user_info_frame = tk.LabelFrame(
    frame,
    text="User Information",
    font=("Poppins Medium", 14),
    fg="#FFFFFF",
    bg="#678983",
)
user_info_frame.grid(row=0, column=0, sticky="news", pady=15, padx=15)

first_name_label = tk.Label(
    user_info_frame, text="First Name", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
first_name_label.grid(row=0, column=0)
middle_name_label = tk.Label(
    user_info_frame,
    text="Middle Name",
    font=("Poppins", 12),
    fg="#FFFFFF",
    bg="#678983",
)
middle_name_label.grid(row=0, column=1)
last_name_label = tk.Label(
    user_info_frame, text="Last Name", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
last_name_label.grid(row=0, column=2)

first_name_entry = tk.Entry(user_info_frame)
middle_name_entry = tk.Entry(user_info_frame)
last_name_entry = tk.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
middle_name_entry.grid(row=1, column=1)
last_name_entry.grid(row=1, column=2)

age_label = tk.Label(
    user_info_frame, text="Age", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=100)
age_label.grid(row=2, column=1)
age_spinbox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# address
address_frame = tk.LabelFrame(
    frame, text="Address", font=("Poppins Medium", 14), fg="#FFFFFF", bg="#678983"
)
address_frame.grid(row=1, column=0, sticky="news", pady=15, padx=15)

barangay_label = tk.Label(
    address_frame, text="Barangay", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
barangay_label.grid(row=1, column=0)
municipality_label = tk.Label(
    address_frame, text="Municipality", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
municipality_label.grid(row=1, column=1)
province_label = tk.Label(
    address_frame, text="Province", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
province_label.grid(row=1, column=2)
region_label = tk.Label(
    address_frame, text="Region", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
region_label.grid(row=3, column=0)
country_label = tk.Label(
    address_frame, text="Country", font=("Poppins", 12), fg="#FFFFFF", bg="#678983"
)
country_label.grid(row=3, column=1)

barangay_entry = tk.Entry(address_frame)
municipality_entry = tk.Entry(address_frame)
province_entry = tk.Entry(address_frame)
region_entry = tk.Entry(address_frame)
country_entry = tk.Entry(address_frame)

barangay_entry.grid(row=2, column=0)
municipality_entry.grid(row=2, column=1)
province_entry.grid(row=2, column=2)
region_entry.grid(row=4, column=0)
country_entry.grid(row=4, column=1)

for widget in address_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# agreement
agreement_frame = tk.LabelFrame(
    frame, text="Agreement", font=("Poppins Medium", 14), fg="#FFFFFF", bg="#678983"
)
agreement_frame.grid(row=2, column=0, sticky="news", pady=15, padx=10)

agreement_var = tk.StringVar(value="Disagree")
agreement_check = tk.Checkbutton(
    agreement_frame,
    text="I agree that all the information I put are all correct.",
    font=("Poppins", 11),
    variable=agreement_var,
    onvalue="Agree",
    offvalue="Disagree",
)
agreement_check.grid(row=1, column=0)

for widget in agreement_frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# submit_button
submit_button = tk.Button(
    frame,
    text="Submit",
    font=("Poppins Medium", 14),
    fg="#FFFFFF",
    bg="#181D31",
    command=submit_data,
)
submit_button.grid(row=3, column=0, sticky="news", pady=15, padx=10)

window.mainloop()
