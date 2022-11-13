import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from budget_controller_app.budget.models import Income, ExpensesInfo

budget_total = Income.objects.filter(author=request.user).aggregate(budget_total=Sum('income'))

expanse_total = ExpensesInfo.objects.filter(author_expanse=request.user).aggregate(expanses=Sum('cost'))
if budget_total['budget_total'] == None:
            budget_total['budget_total'] = 0
if expanse_total['expanses'] == None:
            expanse_total['expanses'] = 0
print(budget_total)
diff = int(budget_total - expanse_total)
fig, ax = plt.subplots()
ax.bar(['Expanses', 'Budget'], [(expanse_total['expanses']), budget_total['budget_total']],
               color=['red', 'green'])
plt.xlabel('Your incomes and expanses')
plt.ylabel('PLN')
ax.set_title('Your total expenses vs total budget')
red_patch = mpatches.Patch(color='red', label='Amount of expanses')
green_patch = mpatches.Patch(color='green', label='Amount of budget')
        ax.legend(handles=[red_patch, green_patch], loc=(0.4, 0.8))
        plt.savefig(os.path.join('test.png'), dpi=90, format='png', bbox_inches='tight')
        plt.switch_backend('agg')
        plt.show()
        plt.close()