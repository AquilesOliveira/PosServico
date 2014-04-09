package controllers;

import java.util.List;

import models.Produto;
import utils.Result;
import api.wadl.annotation.Param;
import api.wadl.annotation.Path;
import api.wadl.annotation.Paths;
import api.wadl.annotation.Resource;
import controllers.restapi.DefaultController;

@Resource(name = "produtos", param = { @Param(name = "{id}", type = "int") })
public class Produtos extends DefaultController {

	@Path(method = "GET", id = "getAllProduto")
	public static void listAll() {
		final List<Produto> produtos = Produto.findAll();
		renderObject(Result.OK(produtos));
	}
        
        @Path(method = "GET", id = "findName")
	public static void findName(final String nome) {
		final List<Produto> produtos = Produto.find("nome = ?", nome).fetch();
                System.out.println("Econtrei o produto: "+produtos.toString());
                renderObject(Result.OK(produtos));
	}
        
	@Path(name = "/{id}", method = "GET", id = "getProdutoById")
	public static void findId(final Long id) {
		if (id != null) {
			final Produto produto = Produto.findById(id);
			if (produto != null) {
				renderObject(Result.OK(produto));
			} else {
				// Registro nao encontrado
				renderObject(Result.ERROR(3));
			}
		} else {
			// Parametro nao informado
			renderObject(Result.ERROR(4));
		}
	}

	@Path(name = "/{id}", method = "DELETE", id = "deleteProduto")
	public static void delete(final Long id) {
		try {
			final Produto produto = Produto.findById(id);
			if (produto != null) {
				produto.delete();
				renderObject(Result.OK("Produto apagado com sucesso."));
			} else {
				// Registro nao encontrado
				renderObject(Result.ERROR(3));
			}
		} catch (final Exception ex) {
			// Erro de sistema
			renderObject(Result.SYSERROR(ex.getMessage()));
		}
	}

	@Paths({
			@Path(method = "POST", id = "addProduto", param = { @Param(name = "produto.nome", type = "string"),
					@Param(name = "produto.descricao", type = "string"), @Param(name = "produto.quantidade", type = "int"),
					@Param(name = "produto.valor", type = "double") }),
			@Path(name = "/{id}", id = "saveProduto", method = "PUT", param = { @Param(name = "produto.nome", type = "string"),
					@Param(name = "produto.descricao", type = "string"), @Param(name = "produto.quantidade", type = "int"),
					@Param(name = "produto.valor", type = "double") }) })
	public static void save(final Long id, Produto produto) {
		if (id != null) {
			final Produto produto_aux = produto;
			produto = Produto.findById(id);
			if (produto != null) {
				produto.nome = produto_aux.nome;
				produto.descricao = produto_aux.descricao;
				produto.quantidade = produto_aux.quantidade;
				produto.valor = produto_aux.valor;
			} else {
				// Registro nao encontrado
				renderObject(Result.ERROR(3));
			}
		}

		validation.valid(produto);

		if (validation.hasErrors()) {
			renderObject(Result.VALIDERROR(validation));
			return;
		}

		final Produto obj_out = produto.save();
		renderObject(Result.OK(obj_out));

	}
}
