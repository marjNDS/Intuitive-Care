SELECT 
    o.razao_social,
    dc.reg_ans,
    SUM(dc.vl_saldo_final) AS total_despesas
FROM public.demonstracoes_contabeis dc
JOIN public.operadoras_ativas o ON o.registro_ans = dc.reg_ans
WHERE LOWER(
    REGEXP_REPLACE(
      TRANSLATE(dc.descricao, 
        'ÁÉÍÓÚÂÊÔÃÕÀÇáéíóúâêôãõàç',
        'AEIOUAEOAOCaeiouaeoaoac'
      ),
      '\s+', ' ', 'g'
    )
  ) LIKE '%sinistros conhecidos ou avisados de assistencia a saude medico hospitalar%'
  AND dc.data >= CURRENT_DATE - INTERVAL '3 months'
GROUP BY o.razao_social, dc.reg_ans
ORDER BY total_despesas DESC
LIMIT 10;
