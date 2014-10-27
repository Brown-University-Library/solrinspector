from . import models
import requests
import mysolr

def get_facets( solr_url, field, optional_params=None):
    solr = models.SolrInspector(solr_url)
    return solr.get_facets_for_field(field, optional_params)

def list_fields(solr_url):
    """docstring for list_fields"""
    solr = models.SolrInspector(solr_url)
    return solr.list_fields()

def main():
    SOLR_URL="http://localhost:8989/solr/fedora_solr/"
    FACET_FIELD = 'mods_type_of_resource'

    print "===============FIELDS=================="
    for field in list_fields(SOLR_URL):
        print field.name, field.count


    print "===============FACETS=================="
    for facet_result in get_facets(SOLR_URL, FACET_FIELD):
        print facet_result.value, facet_result.count

if __name__ == '__main__':
    main()
