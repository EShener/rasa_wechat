from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core.actions.action import ActionListen, ActionRestart

from rasa_core.actions.factories import RemoteAction

from rasa_core.agent import Agent

from rasa_core.train import train_dialogue_model


def test_remote_training(tmpdir):
    train_dialogue_model("examples/remote/concert_domain_remote.yml",
                         "examples/remote/data/stories.md",
                         tmpdir.strpath, {})

    agent = Agent.load(tmpdir.strpath)
    assert agent.domain._factory_name == "remote"

    action_types = [type(a) for a in agent.domain.actions]
    assert action_types[:3] == [ActionListen, ActionRestart, RemoteAction]
