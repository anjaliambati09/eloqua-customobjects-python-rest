import sys
sys.path.append('./lib')
from eloqua_request import EloquaRequest

request = EloquaRequest('BroadridgeFinancialSolutionsInc', 'anjali.ambati', 'Ads@0220')
response = request.get('assets/customObjects', None)
print response
