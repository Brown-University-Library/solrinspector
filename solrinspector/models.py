import requests
import mysolr

class LukeResponse(object):
    """docstring for LukeResponse"""
    def __init__(self, data=None):
        super(LukeResponse, self).__init__()
        self.data = data or {}

    def response_header(self):
        return self.data.get('responseHeader',{})

    def index(self):
        return self.data.get('index',{})

    def info(self):
        return self.data.get('info',{})

    def fields(self):
        return self.data.get('fields',{})

class SolrInspector(mysolr.Solr):

    def _get_luke_url(self, params='numTerms=0&wt=json'):
        """docstring for get_luke_url"""
        return self.base_url + 'admin/luke?%s' % params

    def _get_luke_response(self):
        r = requests.get(self._get_luke_url())
        if not r.ok:
            return []
        return LukeResponse(r.json())

    def _parse_fields(self, field_dict):
        s_fields =sorted(field_dict.items(), key=lambda f: f[1].get('docs',0), reverse=True)
        return [ SolrField( name=k, data=v) for k, v in s_fields]

    def _parse_facet_reults(self, field, facet_result_dict):
        return [ SolrFacetResult(field, value, count) for value, count in facet_result_dict.items()]

    def list_fields(self ):
        luke_response = self._get_luke_response()
        return self._parse_fields(luke_response.fields())

    def get_facets_for_field(self, field, optional_params=None):
        query= {
            'q' : '*:*',
            'facet' : 'true',
            'facet.field' : field,
            'facet.sort': 'index',
        }
        query.update(optional_params or {})
        response = self.search(**query)
        facet_fields = response.facets.get('facet_fields', {})
        facet_result_dict = facet_fields.get(field, {})
        return self._parse_facet_reults(field, facet_result_dict)

class SolrField(object):
    """docstring for SolrField"""
    def __init__(self, name, data=None):
        super(SolrField, self).__init__()
        self.name = name
        self.data = data or {}

    @property
    def count(self):
        return self.data.get('docs',0)

class SolrFacetResult(object):
    """docstring for SolrFacetResult"""
    def __init__(self, field, value, count):
        super(SolrFacetResult, self).__init__()
        self.field = field
        self.value = value
        self.count = count
