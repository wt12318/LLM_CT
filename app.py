import openai
import gradio as gr
import json
openai.api_key = ""

def get_completion_from_messages(messages, model="gpt-3.5-turbo-0613", temperature=0):
    response = openai.ChatCompletion.create(
         model=model,
         messages=messages,
         temperature=temperature, # this is the degree of randomness of the model's output
     )
    return response.choices[0].message["content"]

def get_response(text):
    messages =  [
        {'role':'system', 'content':'You are a paper abstract information extractor, Your task is to perform the following actions:\
        1. the user inputs a paper abstract, and you are responsible for extracting information. \
        The extracted information should write in the form of:  What state of the cancer (this state is usually a mutation in a driver gene) is dependent on which genes or pathways. \
        Do not show other information. When there is no such information (ie. cancer is not dependent on any gene or pathway from the \
        abstract), just return "No dependency". \
        2. Format output as a json object that contains the following keys: cancer, state, gene/pathway. \
        Use the following format: \
        Extracted information: <Extracted information> \
        Output JSON: <json with cancer, state and gene/pathway>. When there is no dependency, do not output JSON'},
        {'role':'user', 'content':'Abstract: In non–small cell lung cancer (NSCLC), \
        concurrent mutations in the oncogene KRAS and the tumor suppressor STK11 encoding the kinase LKB1 result in aggressive tumors \
        prone to metastasis but with liabilities arising from reprogrammed metabolism. \
        We previously demonstrated perturbed nitrogen metabolism and addiction to an unconventional pathway of pyrimidine synthesis in \
        KRAS/LKB1 co-mutant (KL) cancer cells. To gain broader insight into metabolic reprogramming in NSCLC, \
        we analyzed tumor metabolomes in a series of genetically engineered mouse models with oncogenic KRAS combined with mutations in LKB1 or p53. \
        Metabolomics and gene expression profiling pointed towards an activation of the hexosamine biosynthesis pathway (HBP), \
        another nitrogen-related metabolic pathway, in both mouse and human KL mutant tumors. KL cells contain high levels of HBP metabolites, \
        higher flux through the HBP pathway and elevated dependence on the HBP enzyme Glutamine-Fructose-6-Phosphate Transaminase 2 (GFPT2). \
        GFPT2 inhibition selectively reduced KL tumor cell growth in culture, xenografts and genetically-modified mice. \
        Our results define a new metabolic vulnerability in KL tumors and provide a rationale for targeting GFPT2 in this aggressive NSCLC subtype.'},
        {'role':'assistant', 'content':'Extracted information: KRAS/LKB1 co-mutant non–small cell lung cancer is dependent on Hexosamine \
        biosynthesis pathway (HBP) and GFPT2. Output JSON: {"cancer":"non–small cell lung cancer","state":"KRAS/LKB1 co-mutant","gene/pathway":"Hexosamine biosynthesis pathway (HBP) and GFPT2"}'},
        {'role':'user', 'content':'Abstract: Background: Thymidylate synthase (TYMS) is a successful chemotherapeutic target for anticancer therapy. \
        Numerous TYMS inhibitors have been developed and used for treating gastrointestinal cancer now, but they have limited clinical benefits due to \
        the prevalent unresponsiveness and toxicity. It is urgent to identify a predictive biomarker to guide the precise clinical use of TYMS inhibitors. \
        Methods: Genome-scale CRISPR-Cas9 knockout screening was performed to identify potential therapeutic targets for treating gastrointestinal tumours \
        as well as key regulators of raltitrexed (RTX) sensitivity. Cell-based functional assays were used to investigate how \
        MYC regulates TYMS transcription. Cancer patient data were used to verify the correlation between drug response and MYC and/or TYMS mRNA levels. \
        Finally, the role of NIPBL inactivation in gastrointestinal cancer was evaluated in vitro and in vivo. \
        Findings: TYMS is essential for maintaining the viability of gastrointestinal cancer cells, and is selectively inhibited by RTX. \
        Mechanistically, MYC presets gastrointestinal cancer sensitivity to RTX through upregulating TYMS transcription, \
        supported by TCGA data showing that complete response cases to TYMS inhibitors had significantly higher MYC and \
        TYMS mRNA levels than those of progressive diseases. NIPBL inactivation decreases the therapeutic responses of \
        gastrointestinal cancer to RTX through blocking MYC. Interpretation: Our study unveils a mechanism of how TYMS is \
        transcriptionally regulated by MYC, and provides rationales for the precise use of TYMS inhibitors in the clinic.'},
        {'role':'assistant', 'content':'Extracted information: Gastrointestinal cancer with up-regulated MYC is dependent on TYMS. Output JSON: {"cancer":"Gastrointestinal cancer","state":"up-regulated MYC","gene/pathway":"TYMS"}'},
        {'role':'user', 'content':'Abstract: Studies have characterized the immune escape landscape across primary tumors. \
        However, whether late-stage metastatic tumors present differences in genetic immune escape (GIE) prevalence and dynamics remains unclear. \
        We performed a pan-cancer characterization of GIE prevalence across six immune escape pathways in 6,319 uniformly processed tumor samples. \
        To address the complexity of the HLA-I locus in the germline and in tumors, we developed LILAC, an open-source integrative framework. \
        One in four tumors harbors GIE alterations, with high mechanistic and frequency variability across cancer types. \
        GIE prevalence is generally consistent between primary and metastatic tumors. We reveal that GIE alterations are selected for \
        in tumor evolution and focal loss of heterozygosity of HLA-I tends to eliminate the HLA allele, presenting the largest neoepitope repertoire. \
        Finally, high mutational burden tumors showed a tendency toward focal loss of heterozygosity of HLA-I as the immune evasion mechanism, \
        whereas, in hypermutated tumors, other immune evasion strategies prevail.'},
        {'role':'assistant', 'content':'Extracted information: No dependency}'}
    ]
    messages.append({'role':'user', 'content':f"Abstract: {text}"})
    response = get_completion_from_messages(messages, temperature=0)
    return response.split("Output JSON: ")[0], json.loads(response.split("Output JSON: ")[1])

exp = [[
    "Background: Triple-negative breast cancer (TNBC) is an aggressive subtype of breast cancer, \
characterized high rates of tumor protein 53 (p53) mutation and limited targeted therapies. Despite being clinically advantageous, \
direct targeting of mutant p53 has been largely ineffective. Therefore, we hypothesized that there exist pathways upon which p53-mutant \
TNBC cells rely upon for survival. Methods: In vitro and in silico drug screens were used to identify drugs that induced preferential death in \
p53 mutant breast cancer cells. The effects of the glutathione peroxidase 4 (GPX4) inhibitor ML-162 was deleniated using growth and death assays, \
both in vitro and in vivo. The mechanism of ML-162 induced death was determined using small molecule inhibition and genetic knockout. \
Results: High-throughput drug screening demonstrated that p53-mutant TNBCs are highly sensitive to peroxidase,cell cycle, cell division, and \
proteasome inhibitors. We further characterized the effect of the Glutathione . Peroxidase 4 (GPX4) inhibitor ML-162 and demonstrated that \
ML-162 induces preferential ferroptosis in p53-mutant, as compared to p53-wild type, TNBC cell lines. Treatment of p53-mutant xenografts with \
ML-162 suppressed tumor growth and increased lipid peroxidation in vivo. Testing multiple ferroptosis inducers demonstrated p53-missense mutant, \
and not p53-null or wild type cells, were more sensitive to ferroptosis, and that expression of mutant TP53 genes in p53-null cells sensitized \
cells to ML-162 treatment. Finally, we demonstrated that p53-mutation correlates with ALOX15 expression, which rescues ML-162 induced ferroptosis. \
Conclusions: This study demonstrates that p53-mutant TNBC cells have critical, unique survival pathways that can be effectively targeted. \
Our results illustrate the intrinsic vulnerability of p53-mutant TNBCs to ferroptosis, and highlight GPX4 as a promising target for the \
precision treatment of p53-mutant triple-negative breast cancer."
],
["T cells acquire a regulatory phenotype when their T cell antigen receptors (TCRs) experience an intermediate- to high-affinity \
interaction with a self-peptide presented via the major histocompatibility complex (MHC). Using TCRβ sequences from flow-sorted human cells, \
we identified TCR features that promote regulatory T cell (Treg) fate. From these results, we developed a scoring system to quantify TCR-intrinsic \
regulatory potential (TiRP). When applied to the tumor microenvironment, TiRP scoring helped to explain why only some T cell clones maintained the \
conventional T cell (Tconv) phenotype through expansion. To elucidate drivers of these predictive TCR features, we then examined the two elements of the \
Treg TCR ligand separately: the self-peptide and the human MHC class II molecule. These analyses revealed that hydrophobicity in the third \
complementarity-determining region (CDR3β) of the TCR promotes reactivity to self-peptides, while TCR variable gene (TRBV gene) usage shapes the TCR’s \
general propensity for human MHC class II-restricted activation."
]
]

def gradio():

    input_text = gr.inputs.Textbox(label="Input paper abstract")

    output_text = gr.outputs.Textbox(label="Extracted information")

    json_output = gr.JSON(label = "JSON")

    interface = gr.Interface(fn=get_response, inputs=[input_text], outputs=[output_text,json_output], 
                            examples=exp,
                            article="Example abstract from https://doi.org/10.21203/rs.3.rs-1547583/v1 and https://doi.org/10.1038/s41590-022-01129-x")
    interface.launch()


if __name__ == '__main__':
    gradio()
