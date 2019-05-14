OUTPUT := output

all: build

build: $(OUTPUT) $(OUTPUT)/reference/data-acquisition $(OUTPUT)/reference/da-tutorial

$(OUTPUT)/reference/data-acquisition: MOD_DA_REF
	mkdir -p $@ && \
	tar zxvf archives/libmxidaf_c_reference.tar.gz -C $@ && \
	tar zxvf archives/libmxidaf_py_reference.tar.gz -C $@

$(OUTPUT)/reference/da-tutorial: MOD_DA_TUT
	mkdir -p $@ && \
	gitbook build --gitbook=3.2.3 da-tutorial/src/tutorial $@

$(OUTPUT):
	mkdir -p $@
	gitbook build src $(OUTPUT)

MOD_DA_REF:
	sed -i 's|>libmxidaf_c_reference| target="_blank">libmxidaf_c_reference|g' $(OUTPUT)/programming/da-reference/index.html && \
	sed -i 's|>libmxidaf_py_reference| target ="_blank">libmxidaf_py_reference|g' ${OUTPUT}/programming/da-reference/index.html

MOD_DA_TUT:
	sed -i 's|>reference/data-acquisition| target="_blank">reference/data-acquisition|g' $(OUTPUT)/programming/da-tutorial/index.html

clean:
	@rm -rf $(OUTPUT)

.PHONY: book reference
