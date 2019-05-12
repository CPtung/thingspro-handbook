ASTAH_COMMAND=/usr/lib/astah_community/astah-command.sh

.PHONY: all build clean images architecture-images library-design-images tutorial-images

all: daapi-html tutorial-html

daapi-html:
	gitbook build src daapi-html

tutorial-html:
	gitbook build src/tutorial data_acquisition_api_tutorial
	# change icon
	cp -a \
		src/tutorial/images/favicon.ico \
		data_acquisition_api_tutorial/gitbook/images/favicon.ico
	# fix: scrollbar cannot click
	sed -i -e \
		"s/.book .book-body .navigation.navigation-next{right:0}/.book .book-body .navigation.navigation-next{right:18px}/" \
		data_acquisition_api_tutorial/gitbook/style.css
	# pack
	tar zcf \
		data_acquisition_api_tutorial.tar.gz \
		data_acquisition_api_tutorial/


clean:
	rm -rf \
		_book \
		src/architecture/images/architecture \
		src/library-design/images/daapi \
		src/tutorial/images/tutorial \
		daapi-html \
		data_acquisition_api_tutorial \
		*.tar.gz

images: architecture-images library-design-images tutorial-images

architecture-images:
	cd src/architecture/images && \
		${ASTAH_COMMAND} -image all -f architecture.asta -t png -o .

library-design-images:
	cd src/library-design/images && \
		${ASTAH_COMMAND} -image all -f daapi.asta -t png -o .

tutorial-images:
	cd src/tutorial/images && \
		${ASTAH_COMMAND} -image all -f tutorial.asta -t png -o .
