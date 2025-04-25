from _base.analysis import TechnicalAnalyzerABC
import pandas as pd

# Define thresholds
PE_RATIO_THRESHOLD = 15.0
PB_THRESHOLD = 1.5
EV_EBITDA_THRESHOLD = 10.0
UNDERVALUED_THRESHOLD = 3.0

class MetricScore():
    value = 0
    score = 0
    threshold = None
    meets_criteria = False

class TechnicalValuator(TechnicalAnalyzerABC):
    def __init__(self, collector, symbol):
        super(TechnicalValuator, self).__init__(collector)
        self.metrics = {
            'pe': MetricScore(),
            'pb': MetricScore(),
            'dcf': MetricScore(),
            'gv': MetricScore(),
            'ey': MetricScore(),
            'by': MetricScore(),
            'evb': MetricScore(),
            'price': MetricScore()
        }
        self._symbol = symbol
    
    def analyze(self):
        self._collector.set_stock(self._symbol)
        # Collect all values
        self.metrics['pe'].value = self._collector.pe_ratio()
        self.metrics['pb'].value = self._collector.price_to_book()
        self.metrics['dcf'].value = self._collector.dcf()
        self.metrics['gv'].value = self._collector.graham_value()
        self.metrics['ey'].value = self._collector.earnings_yield()
        self.metrics['by'].value = self._collector.bond_yield()
        self.metrics['evb'].value = self._collector.ev_ebitda()
        self.metrics['price'].value = self._collector.get_close()

        # Calculate scores
        self._evaluate_pe()
        self._evaluate_pb()
        self._evaluate_dcf()
        self._evaluate_gv()
        self._evaluate_ey()
        self._evaluate_evb()

        return self._prepare_results()

    def _evaluate_pe(self):
        metric = self.metrics['pe']
        metric.threshold = PE_RATIO_THRESHOLD
        metric.meets_criteria = metric.value < PE_RATIO_THRESHOLD
        metric.score = 1 if metric.meets_criteria else 0

    def _evaluate_pb(self):
        metric = self.metrics['pb']
        metric.threshold = PB_THRESHOLD
        metric.meets_criteria = metric.value < PB_THRESHOLD
        metric.score = 1 if metric.meets_criteria else 0

    def _evaluate_dcf(self):
        metric = self.metrics['dcf']
        metric.threshold = self.metrics['price'].value
        metric.meets_criteria = metric.value < metric.threshold
        metric.score = 1 if metric.meets_criteria else 0

    def _evaluate_gv(self):
        metric = self.metrics['gv']
        metric.threshold = self.metrics['price'].value
        metric.meets_criteria = metric.value < metric.threshold
        metric.score = 1 if metric.meets_criteria else 0

    def _evaluate_ey(self):
        metric = self.metrics['ey']
        metric.threshold = self.metrics['by'].value
        metric.meets_criteria = metric.value > metric.threshold
        metric.score = 1 if metric.meets_criteria else 0

    def _evaluate_evb(self):
        metric = self.metrics['evb']
        metric.threshold = EV_EBITDA_THRESHOLD
        metric.meets_criteria = metric.value < EV_EBITDA_THRESHOLD
        metric.score = 1 if metric.meets_criteria else 0

    def _prepare_results(self):
        total_score = sum(metric.score for name, metric in self.metrics.items() 
                        if name not in ['price', 'by'])
        is_undervalued = total_score >= UNDERVALUED_THRESHOLD
        details = {
            'total_score': total_score
            , 'is_undervalued': is_undervalued
            , 'metrics': {
                name: {
                    'value': metric.value,
                    'score': metric.score,
                    'threshold': metric.threshold,
                    'meets_criteria': metric.meets_criteria
                }
                for name, metric in self.metrics.items()
            }
        }
        
        return details 
        




