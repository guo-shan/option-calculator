import Frontend.Arguments as Arguments
import Frontend.Results as Results
import Frontend.ImpVol as ImpVol
import Frontend.Data as Data
import Frontend.Form as Form

def InitUI(page):
    Arguments.ArgumentsUI(page)
    Results.ResultsUI(page)
    ImpVol.ImpVolUI(page)
    Data.DataUI(page)
    Form.FormUI(page)