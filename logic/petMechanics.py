# from GUI import screen
#
# # Nakarmienie zwierzaka
# def nakarm(jedzenie, postac, najedzenie_progress, label_monety):
#     #todo max 2 razy ten sam pokarm pod rzad
#     #todo uzgodnic poprawne dodawanie jedzenia dla zwierzaka
#     if jedzenie == "woda":
#         postac.najedzenie += 20
#     if jedzenie == "chlep":
#         if postac.monety >= 10:
#             postac.monety -= 10
#             postac.najedzenie += 40
#
#             # tk.Label(root, text="Monety:" + str(postac.monety)).grid(row=3, column=0, columnspan=2)
#     if jedzenie == "ryba":
#         if postac.monety >= 20:
#             postac.monety -= 20
#             postac.najedzenie += 60
#             postac.punkty += 5
#     if jedzenie == "mystery treat":  # todo
#         if postac.monety >= 50:
#             postac.monety -= 50
#             pass
#     najedzenie_progress['value'] = postac.najedzenie
#     label_monety.config(text=f"Monety: {postac.monety}")
#     label_monety.grid(row=3, column=0,columnspan=2)
#
#
# def zabawa():
#     pass