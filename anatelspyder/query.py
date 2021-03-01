# AUTOGENERATED! DO NOT EDIT! File to edit: queries.ipynb (unless otherwise specified).

__all__ = ['MOSAICO', 'RADCOM', 'download_mosaico']

# Cell
import requests
from pathlib import Path

# Cell
MOSAICO = 'http://sistemas.anatel.gov.br/se/public/file/b/srd/estacao_rd.zip'
RADCOM = """
use SITARWEB

select f.MedFrequenciaInicial as 'Frequência',
       uf.SiglaUnidadeFrequencia as 'Unidade',
       es.MedLatitudeDecimal as 'Latitude' ,
	   es.MedLongitudeDecimal as 'Longitude',
       Sitarweb.dbo.FN_SRD_RetornaIndFase(PB.NumServico, Pr.idtPedidoRadcom) as 'Fase',
       Sitarweb.dbo.FN_SRD_RetornaSiglaSituacao(h.IdtHabilitacao, Es.IdtEstacao) as 'Situação',
       es.NumEstacao as 'Numero da Estação',
	   e.NumCnpjCpf as 'CNPJ',
	   e.NomeEntidade as 'Entidade',
	   m.NomeMunicipio as 'Município',
	   pb.SiglaUF as 'UF'	
from ENTIDADE e
inner join HABILITACAO h on h.IdtEntidade = e.IdtEntidade
inner join SRD_PEDIDORADCOM pr on pr.IdtHabilitacao = h.IdtHabilitacao
inner join SRD_PLANOBASICO pb on pb.IdtPlanoBasico = pr.IdtPlanoBasico
inner join estacao es on es.IdtHabilitacao = h.IdtHabilitacao
inner join FREQUENCIA f on f.IdtEstacao = es.IdtEstacao
inner join UnidadeFrequencia uf on uf.IdtUnidadeFrequencia = f.IdtUnidadeFrequencia
inner join Municipio m on m.CodMunicipio = pb.CodMunicipio
where h.NumServico = '231'
"""

# Cell
def download_mosaico():
    file = requests.get(MOSAICO)
    with open(Path.cwd() / 'files' / 'mosaico.zip', 'wb') as mosaico:
        mosaico.write(file.content)