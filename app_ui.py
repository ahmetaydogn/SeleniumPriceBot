import threading
import time

import customtkinter as ct
import main


class App(ct.CTk):
    def __init__(self):
        super().__init__()
        # set app width, height & position
        self.app_width = 380
        self.app_height = 300
        self.x = (self.winfo_screenwidth() - self.app_width) // 2 + ((self.app_width // 2) - 50) # normal tkinter'ı daha kolay şekilde ortalayabiliyoruz fakat bu çalışmıyor niyeyse
        self.y = (self.winfo_screenheight() - self.app_height) // 2
        self.geometry(f"{self.app_width}x{self.app_height}+{self.x}+{self.y}")
        self.resizable(False, False)

        # title, header & fonts
        self.title("FİYAT KARŞILAŞTIRMA BOTU - AHMET AYDOĞAN")
        self.header_font = ('Times New Roman', 24, 'bold')
        self.inputs_font = ('Arial', 14, 'normal')
        self.header_lbl = ct.CTkLabel(self, text='Fiyat Karşılaştırma Botu', font=self.header_font)
        self.header_lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

        # product name(s)
        self.name_lbl = ct.CTkLabel(self, text='Aranacak Ürün(lerin) İsmi: ', font=self.inputs_font)
        self.name_lbl.grid(row=1, column=0, padx=(10, 0), pady=10)
        self.name_entry = ct.CTkEntry(self,width=180)
        self.name_entry.grid(row=1, column=1, padx=(10, 0), pady=10)

        # is wanted one product or not?
        def change_text():
            if self.is_wanted_one_product.get() == 'one_product':
                self.is_wanted_one_product_switch.configure(text='Tek Ürün')
            elif self.is_wanted_one_product.get() == 'all_product':
                self.is_wanted_one_product_switch.configure(text='Çok Ürün')
        self.name_lbl = ct.CTkLabel(self, text='Tek Ürün mü Aratılsın?', font=self.inputs_font)
        self.name_lbl.grid(row=2, column=0, padx=(10, 0), pady=10)
        self.is_wanted_one_product = ct.StringVar(value='one_product')
        self.is_wanted_one_product_switch = ct.CTkSwitch(self, text='Tek Ürün',
                                                         command=change_text,
                                                         variable=self.is_wanted_one_product,
                                                         onvalue="one_product", offvalue="all_product")
        self.is_wanted_one_product_switch.grid(row=2, column=1, padx=(10, 0), pady=10, sticky='e')

        # hepsiburada
        self.hepsiburada_check_var = ct.StringVar(value="hepsiburada_off")
        self.hepsiburada_checkbox = ct.CTkCheckBox(self, text="Hepsiburada", variable=self.hepsiburada_check_var,
                                  onvalue="hepsiburada_on", offvalue="hepsiburada_off")
        self.hepsiburada_checkbox.grid(row=3, column=0, padx=(30,0), pady=10, sticky='w')

        # trendyol
        self.trendyol_check_var = ct.StringVar(value="trendyol_off")
        self.trendyol_checkbox = ct.CTkCheckBox(self, text="Trendyol", variable=self.trendyol_check_var,
                                  onvalue="trendyol_on", offvalue="trendyol_off")
        self.trendyol_checkbox.grid(row=3, column=1, padx=(0,10), pady=10, sticky='e')

        # n11
        self.n11_check_var = ct.StringVar(value="n11_off")
        self.n11_checkbox = ct.CTkCheckBox(self, text="N11", variable=self.n11_check_var,
                                  onvalue="n11_on", offvalue="n11_off")
        self.n11_checkbox.grid(row=4, column=1, padx=(0,10), pady=10, sticky='e')

        # vatanbilgisayar
        self.vatanbilgisayar_check_var = ct.StringVar(value="vatanbilgisayar_off")
        self.vatanbilgisayar_checkbox = ct.CTkCheckBox(self, text="Vatan Bilgisayar", variable=self.vatanbilgisayar_check_var,
                                  onvalue="vatanbilgisayar_on", offvalue="vatanbilgisayar_off")
        self.vatanbilgisayar_checkbox.grid(row=4, column=0, padx=(30,0), pady=10, sticky='w')

        # search button
        def do_something():
            if self.is_wanted_one_product.get() == "one_product":
                self.is_one_product = True
            else:
                self.is_one_product = False

            def run_function(func, *args):
                func(*args)

            threads = []
            if self.hepsiburada_check_var.get() == 'hepsiburada_on':
                thread_hepsiburada = threading.Thread(target=run_function,
                args=(main.search_hepsiburada, self.name_entry.get(), self.is_one_product))

                threads.append(thread_hepsiburada)
                thread_hepsiburada.start()

            if self.trendyol_check_var.get() == 'trendyol_on':
                thread_trendyol = threading.Thread(target=run_function,
                args=(main.search_trendyol, self.name_entry.get(), self.is_one_product))

                threads.append(thread_trendyol)
                thread_trendyol.start()

            if self.n11_check_var.get() == 'n11_on':
                thread_n11 = threading.Thread(target=run_function,
                args=(main.search_n11, self.name_entry.get(), self.is_one_product))

                threads.append(thread_n11)
                thread_n11.start()

            if self.vatanbilgisayar_check_var.get() == 'vatanbilgisayar_on':
                thread_vatanbilgisayar = threading.Thread(target=run_function, args=(
                main.search_vatanbilgisayar, self.name_entry.get(), self.is_one_product))
                threads.append(thread_vatanbilgisayar)
                thread_vatanbilgisayar.start()

            for thread in threads:
                thread.join()


        self.search_button = ct.CTkButton(self, text='Ara', width=310, command=do_something)
        self.search_button.grid(row=5, column=0, columnspan=2, padx=(22, 8), pady=10, sticky='ew')

app = App()
app.mainloop()