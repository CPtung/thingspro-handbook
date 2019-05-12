OUTPUT := ./output

all: book

book: reference

$(OUTPUT):
	mkdir -p $@
	gitbook build src $(OUTPUT)

reference: $(OUTPUT)

clean:
	@rm -rf $(OUTPUT)

.PHONY: book reference
