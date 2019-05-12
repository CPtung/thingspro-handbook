OUTPUT := ./output

all: reference

reference: $(OUTPUT) $(OUTPUT)/reference/data-acquisition $(OUTPUT)/reference/da-tutorial

$(OUTPUT)/reference/data-acquisition:
	mkdir -p $@ && \
	tar zxvf archives/libmxidaf_c_reference.tar.gz -C $@ && \
	tar zxvf archives/libmxidaf_py_reference.tar.gz -C $@

$(OUTPUT)/reference/da-tutorial:
	mkdir -p $@ && \
	gitbook build da-tutorial/src/tutorial $@

$(OUTPUT):
	mkdir -p $@
	gitbook build src $(OUTPUT)

clean:
	@rm -rf $(OUTPUT)

.PHONY: book reference
