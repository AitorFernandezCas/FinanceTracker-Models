"""
Shared models package - independent of any Flask app.
These models can be used in any project that uses SQLAlchemy.
"""
from .base import Base
from .deudas import Deudas
from .inmuebles import Inmuebles
from .liquidez import Liquidez
from .movimientos_bancos import MovimientosBancos
from .hist_compra_instrumentos_financieros import HistCompraInstrumentosFinancieros
from .master.maestro_activos_financieros import MaestroActivosFinancieros
from .master.maestro_bancos import MaestroBancos
from .master.maestro_divisas import MaestroDivisas

__all__ = [
    'Base',
    'Deudas',
    'Inmuebles',
    'Liquidez',
    'HistCompraInstrumentosFinancieros',
    'MaestroActivosFinancieros',
    'MaestroBancos',
    'MaestroDivisas',
    'MovimientosBancos',
]
