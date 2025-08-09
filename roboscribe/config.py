"""Configuration settings for the transcription system."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TranscriptionConfig:
    """Configuration settings for audio transcription model."""

    device: str
    batch_size: int = 16
    compute_type: str = "float16"
    model_name: str = "large-v2"
    language: Optional[str] = None
    vad_filter: bool = True
    diarization_model: str = "pyannote/speaker-diarization-3.1"


@dataclass
class CleanupConfig:
    """Configuration settings for transcript cleanup model."""

    # model_name: str = "meta-llama/Llama-3.1-8B-Instruct"
    model_name: str = "google/gemma-2b-it"
    torch_dtype: str = "bfloat16"
    device_map: str = "auto"
    use_fast_tokenizer: bool = True
    trust_remote_code: bool = False
    revision: str = "main"


@dataclass
class CommandLineArgs:
    """Command line argument configuration."""

    speakers: int
    audio_path: str
    hf_token: str
    output_file: str
