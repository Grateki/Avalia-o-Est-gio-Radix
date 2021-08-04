select
    f.*,
    count(*) as qtd_projetos_encerrados
from
    funcionario f
    inner join funcionario_projeto fp on fp.id_funcionario = f.id_funcionario
    inner join projeto p on fp.id_projeto = p.id_projeto
where
    f.uf = 'RJ' and
    ano_nascimento < year(current_date()) - 20 and
    p.data_fim < current_date()
group by
    f.id_funcionario
having
    count(*) > 3;
