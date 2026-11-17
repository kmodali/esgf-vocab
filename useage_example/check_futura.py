from esgvoc.api import projects

# List all projects
# print(projects.get_all_projects())

# List collections in a project
print(projects.get_all_collections_in_project("cmip7"))

# Get a specific term
term = projects.get_term_in_collection(
    project_id="cmip7",
    collection_id="activity",
    term_id="kmmip"
)
print(term.id)                    # "awesome-alpha"
print(term.drs_name)              # "awesome-alpha"
print(term.description)           # "The first awesome concept"
'''
print(term.awesome_property)      # "alpha-value"
print(term.less_awesome_property) # "optional-alpha"

# Get all terms in a collection
terms = projects.get_all_terms_in_collection(
    project_id="cmip7",
    collection_id="experiment"
)
for t in terms:
    #print(f"{t.id}: {t.drs_name} (awesome_property={t.awesome_property})")
    print(f"{t.id}: {t.drs_name}")
# Search terms by text
results = projects.find_terms_in_project(
    expression="awesome",
    project_id="cordex-cmip6"
)
for r in results:
    print(r.id)
'''
