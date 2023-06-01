'Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции - функции.\
Дополнительно сохраняйте все операции поступления и снятия средств в список'

'Напишите программу банкомат.\
✔ Начальная сумма равна нулю\
✔ Допустимые действия: пополнить, снять, выйти\
✔ Сумма пополнения и снятия кратны 50 у.е.\
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.\
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%\
✔ Нельзя снять больше, чем на счёте\
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой\
операцией, даже ошибочной\
✔ Любое действие выводит сумму денег'

BALANCE = 0
MIN_ = 50
COMMISSION = 0.015
BONUS = 0.03
TAX = 0.10
OPERATION = 0
list_operation = []


def _in(self, cash: int):
    if self.BALANCE > 5_000_000:
        self.BALANCE *= 0.1
    elif cash % self.MIM_ == 0:
        self.BALANCE += cash
        self.OPERATION += 1
        list_operation.append(cash)

    return self.BALANCE


def _out(self, cash: int):
    check_commission = cash + cash*self.COMMiSSION
    if check_commission< 30:
        check_commission = 30
    elif check_commission > 600:
        check_commission = 600
    if self.BALANCE > 5_000_000:
        self.BALANCE *= 0.1
    elif cash % self.MIM_ == 0 and self.BALANCE >= cash + check_commission:
        self.BALANCE -= cash
        self.OPERATION += 1
        list_operation.append(-cash)

    return self.BALANCE


def start(self, mode: str, cash: int) -> str:

    match mode:
        case 'in':
            self._in(cash)
        case 'out':
            self._out(cash)
