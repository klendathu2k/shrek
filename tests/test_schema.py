from pykwalify.core import Core
import os

# pykwalify -d tests/data/EnvironmentBlock.yaml -s schema/Parameters.yaml
def test_environment_block():

    yaml   = "tests/data/Parameters.yaml"
    schema = ["schema/Parameters.yaml"]

    assert(os.path.exists( yaml ) )
    for s in schema:
        assert(os.path.exists(s))

    
    c = Core( source_file=yaml, schema_files=schema)
    c.validate(raise_exception=True)


# pykwalify -d tests/data/InputDataSet.yaml -s schema/InputDataSet.yaml
def test_inputdataset_block():

    yaml   = "tests/data/InputDataSet.yaml"
    schema = ["schema/InputDataSet.yaml"]

    assert(os.path.exists( yaml ) )
    for s in schema:
        assert(os.path.exists(s))
    
    c = Core( source_file=yaml, schema_files=schema)
    c.validate(raise_exception=True)


# pykwalify -d tests/data/OutputDataSet.yaml -s schema/OutputDataSet.yaml
def test_outputdataset_block():

    yaml   = "tests/data/OutputDataSet.yaml"
    schema = ["schema/OutputDataSet.yaml"]

    assert(os.path.exists( yaml ) )
    for s in schema:
        assert(os.path.exists(s))
    
    c = Core( source_file=yaml, schema_files=schema)
    c.validate(raise_exception=True)


# pykwalify -d tests/data/UserCommands.yaml -s schema/UserCommands.yaml
def test_UserCommands_block():

    yaml   = "tests/data/UserCommands.yaml"
    schema = ["schema/UserCommands.yaml"]

    assert(os.path.exists( yaml ) )
    for s in schema:
        assert(os.path.exists(s))
    
    c = Core( source_file=yaml, schema_files=schema)
    c.validate(raise_exception=True)


# pykwalify -d tests/data/JobDefinition.yaml -s schema/JobDefinition.yaml
#def test_JobDefinition_block():
#
#    yaml   = "tests/data/JobDefinition.yaml"
#    schema = ["schema/JobDefinition.yaml"]
#
#    assert(os.path.exists( yaml ) )
#    for s in schema:
#        assert(os.path.exists(s))
#    
#    c = Core( source_file=yaml, schema_files=schema)
#    c.validate(raise_exception=True)
