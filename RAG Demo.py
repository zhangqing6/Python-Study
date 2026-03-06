# 第一步：导入核心库
import os
from langchain_community.document_loaders import DirectoryLoader, DocxLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.llms import Ollama  # 本地大模型（可选）
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 第二步：配置基础路径（按需修改）
DOCS_DIR = "./docs"  # 本地文档文件夹路径
CHROMA_DB_DIR = "./chroma_db"  # 向量数据库存储路径
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # 轻量向量化模型（免费）
# 可选：若用本地大模型（需先安装Ollama并拉取模型），否则替换成OpenAI/文心一言API
LLM_MODEL = "llama3"  # 本地模型（如llama3、qwen等）


# 第三步：核心函数1 - 加载并处理文档
def load_and_split_docs():
    """加载本地文档→切分成小片段"""
    # 1. 加载文档（支持docx/txt，可扩展PDF）
    loaders = []
    for file in os.listdir(DOCS_DIR):
        file_path = os.path.join(DOCS_DIR, file)
        if file.endswith(".docx"):
            loaders.append(DocxLoader(file_path))
        elif file.endswith(".txt"):
            loaders.append(TextLoader(file_path, encoding="utf-8"))

    # 2. 读取文档内容
    docs = []
    for loader in loaders:
        docs.extend(loader.load())

    # 3. 切分文档（避免单片段过长，影响检索和回答）
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,  # 每个片段500字
        chunk_overlap=50,  # 片段重叠50字，保证上下文连贯
        separators=["\n\n", "\n", "。", "！", "？", "，", " "]  # 按中文分隔
    )
    splits = text_splitter.split_documents(docs)
    print(f"文档加载完成，切分成 {len(splits)} 个片段")
    return splits


# 第四步：核心函数2 - 构建向量数据库
def build_vector_db():
    """文档片段→向量化→存入Chroma"""
    # 1. 加载向量化模型
    embeddings = SentenceTransformerEmbeddings(model_name=EMBEDDING_MODEL)

    # 2. 加载/构建向量库（若已存在则加载，否则新建）
    if os.path.exists(CHROMA_DB_DIR):
        vectordb = Chroma(persist_directory=CHROMA_DB_DIR, embedding_function=embeddings)
        print("加载已存在的向量数据库")
    else:
        splits = load_and_split_docs()
        vectordb = Chroma.from_documents(
            documents=splits,
            embedding=embeddings,
            persist_directory=CHROMA_DB_DIR
        )
        vectordb.persist()  # 保存向量库到本地
        print("新建向量数据库并保存")
    return vectordb


# 第五步：核心函数3 - 构建RAG问答链
def build_rag_chain(vectordb):
    """检索→拼接上下文→大模型生成回答"""
    # 1. 检索器：从向量库找最相关的3个文档片段
    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # 2. 本地大模型（替换成LLM API见下方说明）
    llm = Ollama(model=LLM_MODEL)

    # 3. 提示词模板（告诉大模型：基于检索到的内容回答）
    prompt = PromptTemplate.from_template("""
    请基于以下参考内容回答用户的问题，只使用参考内容中的信息，不要编造：
    参考内容：
    {context}

    用户问题：{question}
    """)

    # 4. 构建RAG链：检索→拼接上下文→大模型→解析结果
    rag_chain = (
            {"context": retriever, "question": RunnablePassthrough()}
            | prompt
            | llm
            | StrOutputParser()
    )
    return rag_chain


# 第六步：主函数 - 运行问答
if __name__ == "__main__":
    # 1. 构建向量数据库
    vectordb = build_vector_db()

    # 2. 构建RAG问答链
    rag_chain = build_rag_chain(vectordb)

    # 3. 交互式问答
    print("\n=== 本地文档问答机器人 ===")
    print("输入'退出'结束对话")
    while True:
        question = input("\n请提问：")
        if question.strip() == "退出":
            break
        # 调用RAG链获取回答
        answer = rag_chain.invoke(question)
        print(f"\n回答：{answer}")